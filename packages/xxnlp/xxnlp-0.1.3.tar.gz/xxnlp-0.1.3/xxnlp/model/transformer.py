import torch
import torch.nn as nn
import torch.nn.functional as F
import math
from xxnlp.model import seq_len_to_mask
from fastNLP.modules.torch import TransformerSeq2SeqEncoder


class TimeformerEncoder(TransformerSeq2SeqEncoder):

    def __init__(self, embed: nn.Module, d_model: int = 512, num_layers: int = 6, n_head: int = 8, dim_ff: int = 2048, dropout: float = 0.1, use_time=True):
        super().__init__(embed, None, d_model, num_layers, n_head, dim_ff, dropout)
        self.position_vec = nn.Parameter(torch.tensor(
            [math.pow(10000.0, 2.0 * (i // 2) / d_model) for i in range(d_model)]
        ), requires_grad=False)
        self.use_time = use_time

    def forward(self, tokens, seq_len, time=None):
        x = self.embed(tokens) * self.embed_scale  # batch, seq, dim
        max_src_len = x.size(1)
        x = self.input_fc(x); device = x.device
        x = F.dropout(x, p=self.dropout, training=self.training)
        encoder_mask = seq_len_to_mask(seq_len, max_len=max_src_len).to(device)
        if not self.use_time:
            time = torch.arange(1, max_src_len+1).unsqueeze(0).long().to(device)
        time_enc = self.temporal_enc(time, encoder_mask)
        for layer in self.layer_stacks:
            x += time_enc
            x = layer(x, encoder_mask)
        x = self.layer_norm(x)
        return x, encoder_mask

    def temporal_enc(self, time, non_pad_mask):
        """
        Input: batch*seq_len.
        Output: batch*seq_len*d_model.
        """
        result = time.unsqueeze(-1) / self.position_vec
        result[:, :, 0::2] = torch.sin(result[:, :, 0::2])
        result[:, :, 1::2] = torch.cos(result[:, :, 1::2])
        return result * non_pad_mask.unsqueeze(-1)


class Sparsemax(nn.Module):
    __constants__ = ["dim"]

    def __init__(self, dim=-1):
        """
        Sparsemax class as seen in https://arxiv.org/pdf/1602.02068.pdf
        Parameters
        ----------
        dim: The dimension we want to cast the operation over. Default -1
        """
        super(Sparsemax, self).__init__()
        self.dim = dim

    def __setstate__(self, state):
        self.__dict__.update(state)
        if not hasattr(self, "dim"):
            self.dim = None

    def forward(self, input):
        return SparsemaxFunction.apply(input, self.dim)

    def extra_repr(self):
        return f"dim={self.dim}"


class Sparsemax(nn.Module):
    __constants__ = ["dim"]

    def __init__(self, dim=-1):
        """
        Sparsemax class as seen in https://arxiv.org/pdf/1602.02068.pdf
        Parameters
        ----------
        dim: The dimension we want to cast the operation over. Default -1
        """
        super(Sparsemax, self).__init__()
        self.dim = dim

    def __setstate__(self, state):
        self.__dict__.update(state)
        if not hasattr(self, "dim"):
            self.dim = None

    def forward(self, input):
        return SparsemaxFunction.apply(input, self.dim)

    def extra_repr(self):
        return f"dim={self.dim}"


class SparsemaxFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input: torch.Tensor, dim: int = -1):
        input_dim = input.dim()
        if input_dim <= dim or dim < -input_dim:
            raise IndexError(
                f"Dimension out of range (expected to be in range of [-{input_dim}, {input_dim - 1}], but got {dim})"
            )

        # Save operating dimension to context
        ctx.needs_reshaping = input_dim > 2
        ctx.dim = dim

        if ctx.needs_reshaping:
            ctx, input = flatten_all_but_nth_dim(ctx, input)

        # Translate by max for numerical stability
        input = input - input.max(-1, keepdim=True).values.expand_as(input)

        zs = input.sort(-1, descending=True).values
        range = torch.arange(1, input.size()[-1] + 1)
        range = range.expand_as(input).to(input)

        # Determine sparsity of projection
        bound = 1 + range * zs
        is_gt = bound.gt(zs.cumsum(-1)).type(input.dtype)
        k = (is_gt * range).max(-1, keepdim=True).values

        # Compute threshold
        zs_sparse = is_gt * zs

        # Compute taus
        taus = (zs_sparse.sum(-1, keepdim=True) - 1) / k
        taus = taus.expand_as(input)

        output = torch.max(torch.zeros_like(input), input - taus)

        # Save context
        ctx.save_for_backward(output)

        # Reshape back to original shape
        if ctx.needs_reshaping:
            ctx, output = unflatten_all_but_nth_dim(ctx, output)

        return output

    @staticmethod
    def backward(ctx, grad_output):
        output, *_ = ctx.saved_tensors

        # Reshape if needed
        if ctx.needs_reshaping:
            ctx, grad_output = flatten_all_but_nth_dim(ctx, grad_output)

        # Compute gradient
        nonzeros = torch.ne(output, 0)
        num_nonzeros = nonzeros.sum(-1, keepdim=True)
        sum = (grad_output * nonzeros).sum(-1, keepdim=True) / num_nonzeros
        grad_input = nonzeros * (grad_output - sum.expand_as(grad_output))

        # Reshape back to original shape
        if ctx.needs_reshaping:
            ctx, grad_input = unflatten_all_but_nth_dim(ctx, grad_input)

        return grad_input, None

        
# --------------------- utility start -----------------------------------------
def flatten_all_but_nth_dim(ctx, x: torch.Tensor):
    """
    Flattens tensor in all but 1 chosen dimension.
    Saves necessary context for backward pass and unflattening.
    """

    # transpose batch and nth dim
    x = x.transpose(0, ctx.dim)

    # Get and save original size in context for backward pass
    original_size = x.size()
    ctx.original_size = original_size

    # Flatten all dimensions except nth dim
    x = x.reshape(x.size(0), -1)

    # Transpose flattened dimensions to 0th dim, nth dim to last dim
    return ctx, x.transpose(0, -1)


def unflatten_all_but_nth_dim(ctx, x: torch.Tensor):
    """
    Unflattens tensor using necessary context
    """
    # Tranpose flattened dim to last dim, nth dim to 0th dim
    x = x.transpose(0, 1)

    # Reshape to original size
    x = x.reshape(ctx.original_size)

    # Swap batch dim and nth dim
    return ctx, x.transpose(0, ctx.dim)
# --------------------- utility end -----------------------------------------


if __name__ == '__main__':
    from torch.autograd import gradcheck
    sparsemax = Sparsemax(dim=-1)
    softmax = torch.nn.Softmax(dim=-1)
    logits = torch.randn(2,3,5, requires_grad=True, dtype=torch.double)
    soft_prob, sparse_prob = softmax(logits), sparsemax(logits)
    assert gradcheck(sparsemax, logits, eps=1e-6, atol=1e-4) is True
    print(
        f"""
        softmax[0,0]            {soft_prob[0,0].round(decimals=3).tolist()}       
        sparsemax[0,0]          {sparse_prob[0,0].round(decimals=3).tolist()}       
        """
    )
import numpy as np
import pandas as pd
from typing import Sequence

def describe(**kwargs):
    """each value must be a list"""
    dfs = []
    for k, data in kwargs.items():
        if not isinstance(data, Sequence): continue
        dfs.append(pd.DataFrame({k: data}).describe())
    return pd.concat(dfs, axis=1).T

def statistics(lst):
    """a list of numbers, get their statistics"""
    if not lst: return {}
    fq = lambda q: np.quantile(lst, q)
    return dict(
        mu=np.mean(lst), std=np.std(lst), min=np.min(lst), max=np.max(lst), 
        q25=fq(0.25), q50=fq(0.5), q75=fq(0.75)
    )
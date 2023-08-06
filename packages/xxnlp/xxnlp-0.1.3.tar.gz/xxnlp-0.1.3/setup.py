# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xxnlp',
 'xxnlp.configs',
 'xxnlp.data',
 'xxnlp.keras',
 'xxnlp.model',
 'xxnlp.project.erisk',
 'xxnlp.project.exp',
 'xxnlp.project.micro',
 'xxnlp.project.micro.aggregators',
 'xxnlp.project.micro.micromodels',
 'xxnlp.project.toxic',
 'xxnlp.project.toxic.data',
 'xxnlp.project.toxic.data.augmentations',
 'xxnlp.project.toxic.modelling',
 'xxnlp.project.toxic.modelling.modules',
 'xxnlp.project.toxic.utils',
 'xxnlp.project.twitter',
 'xxnlp.project.twitter.pseudodata',
 'xxnlp.skorch',
 'xxnlp.spacy',
 'xxnlp.spacy.clausecat',
 'xxnlp.tests.twitter',
 'xxnlp.tools',
 'xxnlp.torch',
 'xxnlp.torch.ignite',
 'xxnlp.torch.nlp',
 'xxnlp.torch.trainer',
 'xxnlp.types',
 'xxnlp.utils']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'xxnlp',
    'version': '0.1.3',
    'description': '',
    'long_description': '# XNLP\n\n首先是document embedding: 怎么把原始的一个段落/推文给转换成一个embedding, 这里有很多的Embedding模型(bert,xlnet,)和sentence-embedding模型\n\n在得到了段落的embedding基础上, 下一步是怎么把信息给整合起来, 这里可以用attn+lstm或者transformer',
    'author': 'dennislblog',
    'author_email': 'dennisl@udel.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
}


setup(**setup_kwargs)

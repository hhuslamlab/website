---
title: "Hard Non-Monotonic Attention for Character-Level Transduction"
date: 2018-10-01
publishDate: 2021-08-20T18:07:25.627764Z
authors: ["Shijie Wu", "Pamela Shapiro", "Ryan Cotterell"]
publication_types: ["1"]
abstract: "Character-level string-to-string transduction is an important component of various NLP tasks. The goal is to map an input string to an output string, where the strings may be of different lengths and have characters taken from different alphabets. Recent approaches have used sequence-to-sequence models with an attention mechanism to learn which parts of the input string the model should focus on during the generation of the output string. Both soft attention and hard monotonic attention have been used, but hard non-monotonic attention has only been used in other sequence modeling tasks and has required a stochastic approximation to compute the gradient. In this work, we introduce an exact, polynomial-time algorithm for marginalizing over the exponential number of non-monotonic alignments between two strings, showing that hard attention models can be viewed as neural reparameterizations of the classical IBM Model 1. We compare soft and hard non-monotonic attention experimentally and find that the exact algorithm significantly improves performance over the stochastic approximation and outperforms soft attention."
featured: false
publication: "*Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing*"
publication_short: "EMNLP"
links:
- name: Anthology
  url: https://www.aclweb.org/anthology/P19-1148/
- name: arXiv
  url: https://arxiv.org/abs/1808.10024
url_pdf: papers/wu+al.emnlp18.pdf
---


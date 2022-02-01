---
title: "Determinantal Beam Search"
date: 2021-08-01
publishDate: 2021-10-08T07:56:31.353070Z
authors: ["Clara Meister", "Martina Forster", "Ryan Cotterell"]
publication_types: ["1"]
abstract: "Beam search is a go-to strategy for decoding neural sequence models. The algorithm can naturally be viewed as a subset optimization problem, albeit one where the corresponding set function does not reflect interactions between candidates. Empirically, this leads to sets often exhibiting high overlap, e.g., strings may differ by only a single word. Yet in use-cases that call for multiple solutions, a diverse or representative set is often desired. To address this issue, we propose a reformulation of beam search, which we call determinantal beam search. Determinantal beam search has a natural relationship to determinantal point processes (DPPs), models over sets that inherently encode intra-set interactions. By posing iterations in beam search as a series of subdeterminant maximization problems, we can turn the algorithm into a diverse subset selection process. In a case study, we use the string subsequence kernel to explicitly encourage n-gram coverage in text generated from a sequence model. We observe that our algorithm offers competitive performance against other diverse set generation strategies in the context of language generation, while providing a more general approach to optimizing for diversity."
featured: false
publication: "*Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 10th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)*"
publication_short: "ACL"
links:
- name: Anthology
  url: https://aclanthology.org/2021.acl-long.512.pdf
- name: arXiv
  url: https://arxiv.org/abs/2106.07400
url_pdf: papers/meister+al.acl21a.pdf
url_code: https://github.com/rycolab/swor/tree/diverse_decoding
---


---
title: "Efficient Sampling of Dependency Structure"
date: 2021-11-01
publishDate: 2021-10-08T07:56:33.451426Z
authors: ["Ran Zmigrod", "Tim Vieira", "Ryan Cotterell"]
publication_types: ["1"]
abstract: "Probabilistic distributions over spanning trees in directed graphs are a fundamental model of dependency structure in natural language processing, syntactic dependency trees. In NLP, dependency trees often have an additional root constraint: only one edge may emanate from the root. However, no sampling algorithm has been presented in the literature to account for this additional constraint. In this paper, we adapt two spanning tree sampling algorithms to faithfully sample dependency trees from a graph subject to the root constraint. Wilson (1996)'s sampling algorithm has a running time of O(H) where H is the mean hitting time of the graph. Colbourn (1996)'s sampling algorithm has a running time of O(N^3), which is often greater than the mean hitting time of a directed graph. Additionally, we build upon Colbourn's algorithm and present a novel extension that can sample K trees without replacement in O(K N^3 + K^2 N) time. To the best of our knowledge, no algorithm has been given for sampling spanning trees without replacement from a directed graph."
featured: true
publication: "*Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing*"
publication_short: "EMNLP"
links:
- name: arXiv
  url: https://arxiv.org/abs/2109.06521
url_pdf: papers/zmigrod+al.emnlp21.pdf
url_code: https://github.com/rycolab/treesample
---


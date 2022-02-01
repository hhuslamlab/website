---
title: "On Finding the $K$-best Non-projective Dependency Trees"
date: 2021-08-01
publishDate: 2021-10-08T07:56:31.209651Z
authors: ["Ran Zmigrod", "Tim Vieira", "Ryan Cotterell"]
publication_types: ["1"]
abstract: "The connection between the maximum spanning tree in a directed graph and the best dependency tree of a sentence has been exploited by the NLP community. However, for many dependency parsing schemes, an important detail of this approach is that the spanning tree must have exactly one edge emanating from the root. While work has been done to efficiently solve this problem for finding the one-best dependency tree, no research has attempted to extend this solution to finding the K-best dependency trees. This is arguably a more important extension as a larger proportion of decoded trees will not be subject to the root constraint of dependency trees. Indeed, we show that the rate of root constraint violations increases by an average of 13 times when decoding with K=50 as opposed to K=1. In this paper, we provide a simplification of the K-best spanning tree algorithm of Camerini et al. (1980). Our simplification allows us to obtain a constant time speed-up over the original algorithm. Furthermore, we present a novel extension of the algorithm for decoding the K-best dependency trees of a graph which are subject to a root constraint."
featured: false
publication: "*Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 10th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)*"
publication_short: "ACL"
links:
- name: Anthology
  url: https://aclanthology.org/2021.acl-long.106.pdf
- name: arXiv
  url: https://arxiv.org/abs/2106.00780
url_pdf: papers/zmigrod+al.acl21a.pdf
url_code: https://github.com/rycolab/spanningtrees
---


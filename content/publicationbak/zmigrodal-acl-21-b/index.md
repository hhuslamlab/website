---
title: "Higher-order Derivatives of Weighted Finite-state Machines"
date: 2021-08-01
publishDate: 2021-10-08T07:56:31.505921Z
authors: ["Ran Zmigrod", "Tim Vieira", "Ryan Cotterell"]
publication_types: ["1"]
abstract: "Weighted finite-state machines are a fundamental building block of NLP systems. They have withstood the test of time—from their early use in noisy channel models in the 1990s up to modern-day neurally parameterized conditional random fields. This work examines the computation of higher-order derivatives with respect to the normalization constant for weighted finite-state machines. We provide a general algorithm for evaluating derivatives of all orders, which has not been previously described in the literature. In the case of second-order derivatives, our scheme runs in the optimal O(Aˆ2 Nˆ4) time where A is the alphabet size and N is the number of states. Our algorithm is significantly faster than prior algorithms. Additionally, our approach leads to a significantly faster algorithm for computing second-order expectations, such as covariance matrices and gradients of first-order expectations."
featured: false
publication: "*Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 10th International Joint Conference on Natural Language Processing (Volume 2: Short Papers)*"
publication_short: "ACL"
links:
- name: Anthology
  url: https://aclanthology.org/2021.acl-short.32.pdf
- name: arXiv
  url: https://arxiv.org/abs/2106.00749
url_pdf: papers/zmigrod+al.acl21b.pdf
url_code: https://github.com/rycolab/wfsm
---


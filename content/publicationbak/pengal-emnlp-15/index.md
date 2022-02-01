---
title: "Dual Decomposition Inference for Graphical Models over Strings"
date: 2015-09-01
publishDate: 2021-08-20T18:07:10.261959Z
authors: ["Nanyun Peng", "Ryan Cotterell", "Jason Eisner"]
publication_types: ["1"]
abstract: "We investigate dual decomposition for joint MAP inference of many strings. Given an arbitrary graphical model, we decompose it into small acyclic sub-models, whose MAP configurations can be found by finite-state composition and dynamic programming. We force the solutions of these subproblems to agree on overlapping variables, by tuning Lagrange multipliers for an adaptively expanding set of variable-length n-gram count features.  This is the first inference method for arbitrary graphical models over strings that does not require approximations such as random sampling, message simplification, or a bound on string length. Provided that the inference method terminates, it gives a certificate of global optimality (though MAP inference in our setting is undecidable in general). On our global phonological inference problems, it always terminates, and achieves more accurate results than max-product and sum-product loopy belief propagation."
featured: false
publication: "*Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing*"
publication_short: "EMNLP"
links:
- name: Anthology
  url: https://www.aclweb.org/anthology/D15-1272.pdf
url_pdf: papers/peng+al.emnlp15.pdf
---


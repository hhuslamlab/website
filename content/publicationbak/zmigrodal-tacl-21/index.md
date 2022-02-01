---
title: "Efficient Computation of Expectations under Spanning Tree Distributions"
date: 2021-01-01
publishDate: 2021-10-08T07:56:35.450783Z
authors: ["Ran Zmigrod", "Tim Vieira", "Ryan Cotterell"]
publication_types: ["2"]
abstract: "We give a general framework for inference in spanning tree models. We propose unified algorithms for the important cases of first-order expectations and second-order expectations in edge-factored, non-projective spanning-tree models. Our algorithms exploit a fundamental connection between gradients and expectations, which allows us to derive efficient algorithms. These algorithms are easy to implement with or without automatic differentiation software. We motivate the development of our framework with several cautionary tales of previous research, which has developed numerous inefficient algorithms for computing expectations and their gradients. We demonstrate how our framework efficiently computes several quantities with known algorithms, including the expected attachment score, entropy, and generalized expectation criteria. As a bonus, we give algorithms for quantities that are missing in the literature, including the KL divergence. In all cases, our approach matches the efficiency of existing algorithms and, in several cases, reduces the runtime complexity by a factor of the sentence length. We validate the implementation of our framework through runtime experiments. We find our algorithms are up to 15 and 9 times faster than previous algorithms for computing the Shannon entropy and the gradient of the generalized expectation objective, respectively."
featured: true
publication: "*Transactions of the Association for Computational Linguistics*"
publication_short: "TACL"
links:
- name: Anthology
  url: https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00391/102843/Efficient-Computation-of-Expectations-under
- name: arXiv
  url: https://arxiv.org/abs/2008.12988
url_pdf: papers/zmigrod+al.tacl21.pdf
url_code: https://github.com/rycolab/tree_expectations
---


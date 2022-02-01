---
title: "It’s All in the Name: Mitigating Gender Bias with Name-Based Counterfactual Data Substitution"
date: 2019-11-01
publishDate: 2021-08-20T18:07:29.815618Z
authors: ["Rowan Hall Maudslay", "Hila Gonen", "Ryan Cotterell", "Simone Teufel"]
publication_types: ["1"]
abstract: "This paper treats gender bias latent in word embeddings. Previous mitigation attempts rely on the operationalisation of gender bias as a projection over a linear subspace. An alternative approach is Counterfactual Data Augmentation (CDA), in which a corpus is duplicated and augmented to remove bias, e.g. by swapping all inherently-gendered words in the copy. We perform an empirical comparison of these approaches on the English Gigaword and Wikipedia, and find that whilst both successfully reduce direct bias and perform well in tasks which quantify embedding quality, CDA variants outperform projection-based methods at the task of drawing non-biased gender analogies by an average of 19% across both corpora. We propose two improvements to CDA: Counterfactual Data Substitution (CDS), a variant of CDA in which potentially biased text is randomly substituted to avoid duplication, and the Names Intervention, a novel name-pairing technique that vastly increases the number of words being treated. CDA/S with the Names Intervention is the only approach which is able to mitigate indirect gender bias: following debiasing, previously biased words are significantly less clustered according to gender (cluster purity is reduced by 49%), thus improving on the state-of-the-art for bias mitigation."
featured: false
publication: "*Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing*"
publication_short: "EMNLP"
links:
- name: Anthology
  url: https://www.aclweb.org/anthology/D19-1530.pdf
- name: arXiv
  url: https://arxiv.org/abs/1909.00871
url_pdf: papers/hall-maudslay+al.emnlp-ijcnlp19.pdf
---


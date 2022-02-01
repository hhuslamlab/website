---
title: "Parameter Space Factorization for Zero-Shot Learning across Tasks and Languages"
date: 2021-01-01
publishDate: 2021-10-08T07:56:35.000948Z
authors: ["Edoardo M. Ponti", "Ivan Vulić", "Ryan Cotterell", "Marinela Parović", "Roi Reichart", "Anna Korhonen"]
publication_types: ["2"]
abstract: "Most combinations of NLP tasks and language varieties lack in-domain examples for supervised training because of the paucity of annotated data. How can neural models make sample-efficient generalizations from task-language combinations with available data to low-resource ones? In this work, we propose a Bayesian generative model for the space of neural parameters. We assume that this space can be factorized into latent variables for each language and each task. We infer the posteriors over such latent variables based on data from seen task-language combinations through variational inference. This enables zero-shot classification on unseen combinations at prediction time. For instance, given training data for named entity recognition (NER) in Vietnamese and for part-of-speech (POS) tagging in Wolof, our model can perform accurate predictions for NER in Wolof. In particular, we experiment with a typologically diverse sample of 33 languages from 4 continents and 11 families, and show that our model yields comparable or better results than state-of-the-art, zero-shot cross-lingual transfer methods. Our code is available at https://github.com/cambridgeltl/parameter-factorization."
featured: false
publication: "*Transactions of the Association for Computational Linguistics*"
publication_short: "TACL"
links:
- name: Anthology
  url: https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00374/100681/Parameter-Space-Factorization-for-Zero-Shot
- name: arXiv
  url: https://arxiv.org/abs/2001.11453
url_pdf: papers/ponti+al.tacl21.pdf
url_code: https://github.com/cambridgeltl/parameter-factorization
---


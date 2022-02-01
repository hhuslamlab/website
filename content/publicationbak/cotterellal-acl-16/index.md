---
title: "Morphological Smoothing and Extrapolation of Word Embeddings"
date: 2016-08-01
publishDate: 2021-08-20T18:07:14.202616Z
authors: ["Ryan Cotterell", "Hinrich Schütze", "Jason Eisner"]
publication_types: ["1"]
abstract: "Languages with rich inflectional morphology exhibit lexical data sparsity, since the word used to express a given concept will vary with the syntactic context. For instance, each count noun in Czech has 12 forms (where English uses only singular and plural). Even in large corpora, we are unlikely to observe all inflections of a given lemma. This reduces the vocabulary coverage of methods that induce continuous representations for words from distributional corpus information. We solve this problem by exploiting existing morphological resources that can enumerate a word’s component morphemes. We present a latent variable Gaussian graphical model that allows us to extrapolate continuous representations for words not observed in the training corpus, as well as smoothing the representations provided for the observed words. The latent variables represent embeddings of morphemes, which combine to create embeddings of words. Over several languages and training sizes, our model improves the embeddings for words, when evaluated on an analogy task, skip-gram predictive accuracy, and word similarity"
featured: false
publication: "*Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics*"
publication_short: "ACL"
links:
- name: Anthology
  url: https://www.aclweb.org/anthology/P16-1156/
url_pdf: papers/cotterell+al.acl16.pdf
---


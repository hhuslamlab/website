---
title: "Modeling the Unigram Distribution"
date: 2021-08-01
publishDate: 2021-10-08T07:56:33.632859Z
authors: ["Irene Nikkarinen*", "Tiago Pimentel*", "Damián Blasi", "Ryan Cotterell"]
publication_types: ["1"]
abstract: "The unigram distribution is the non-contextual probability of finding a specific word form in a corpus. While of central importance to the study of language, it is commonly approximated by each word's sample frequency in the corpus. This approach, being highly dependent on sample size, assigns zero probability to any out-of-vocabulary (oov) word form. As a result, it produces negatively biased probabilities for any oov word form, while positively biased probabilities to in-corpus words. In this work, we argue in favor of properly modeling the unigram distribution -- claiming it should be a central task in natural language processing. With this in mind, we present a novel model for estimating it in a language (a neuralization of Goldwater et al.'s (2011) model) and show it produces much better estimates across a diverse set of 7 languages than the naïve use of neural character-level language models."
featured: false
publication: "*Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021*"
publication_short: "Findings of ACL"
links:
- name: Anthology
  url: https://aclanthology.org/2021.findings-acl.326/
- name: arXiv
  url: https://arxiv.org/abs/2106.02289
url_pdf: papers/nikkarinen+al.acl-findings21.pdf
url_code: https://github.com/irenenikk/modelling-unigram
---


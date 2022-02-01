---
title: "Do Syntactic Probes Probe Syntax? Experiments with Jabberwocky Probing"
date: 2021-06-01
publishDate: 2021-10-08T07:56:34.118132Z
authors: ["Rowan Hall Mauslay", "Ryan Cotterell"]
publication_types: ["1"]
abstract: "Analysing whether neural language models encode linguistic information has become popular in NLP. One method of doing so, which is frequently cited to support the claim that models like BERT encode syntax, is called probing; probes are small supervised models trained to extract linguistic information from another model's output. If a probe is able to predict a particular structure, it is argued that the model whose output it is trained on must have implicitly learnt to encode it. However, drawing a generalisation about a model's linguistic knowledge about a specific phenomena based on what a probe is able to learn may be problematic: in this work, we show that semantic cues in training data means that syntactic probes do not properly isolate syntax. We generate a new corpus of semantically nonsensical but syntactically well-formed Jabberwocky sentences, which we use to evaluate two probes trained on normal data. We train the probes on several popular language models (BERT, GPT-2, and RoBERTa), and find that in all settings they perform worse when evaluated on these data, for one probe by an average of 15.4 UUAS points absolute. Although in most cases they still outperform the baselines, their lead is reduced substantially, e.g. by 53% in the case of BERT for one probe. This begs the question: what empirical scores constitute knowing syntax?"
featured: false
publication: "*Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*"
publication_short: "NAACL"
links:
- name: Anthology
  url: https://aclanthology.org/2021.naacl-main.11.pdf
- name: arXiv
  url: https://arxiv.org/abs/2106.02559
url_pdf: papers/hall-mauslay+al.naacl21.pdf
url_code: https://github.com/rowanhm/jabberwocky-probing
---


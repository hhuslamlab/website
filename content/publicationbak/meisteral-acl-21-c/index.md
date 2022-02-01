---
title: "Language Model Evaluation Beyond Perplexity"
date: 2021-08-01
publishDate: 2021-10-08T07:56:31.945458Z
authors: ["Clara Meister", "Ryan Cotterell"]
publication_types: ["1"]
abstract: "We propose an alternate approach to quantifying how well language models learn natural language: we ask how well they match the statistical tendencies of natural language. To answer this question, we analyze whether text generated from language models exhibits the statistical tendencies present in the human-generated text on which they were trained. We provide a framework--paired with significance tests--for evaluating the fit of language models to these trends. We find that neural language models appear to learn only a subset of the tendencies considered, but align much more closely with empirical trends than proposed theoretical distributions (when present). Further, the fit to different distributions is highly-dependent on both model architecture and generation strategy. As concrete examples, text generated under the nucleus sampling scheme adheres more closely to the type--token relationship of natural language than text produced using standard ancestral sampling; text from LSTMs reflects the natural language distributions over length, stopwords, and symbols surprisingly well."
featured: false
publication: "*Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 10th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)*"
publication_short: "ACL"
links:
- name: Anthology
  url: https://aclanthology.org/2021.acl-long.414.pdf
- name: arXiv
  url: https://arxiv.org/abs/2106.00085
url_pdf: papers/meister+al.acl21c.pdf
---


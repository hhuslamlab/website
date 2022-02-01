---
title: "The Paradigm Discovery Problem"
date: 2020-07-01
publishDate: 2021-10-08T07:56:40.391816Z
authors: ["Alexander Erdmann", "Micha Elsner", "Shijie Wu", "Ryan Cotterell", "Nizar Habash"]
publication_types: ["1"]
abstract: "This work treats the paradigm discovery problem (PDP)—the task of learning an inflectional morphological system from unannotated sentences. We formalize the PDP and develop evaluation metrics for judging systems. Using currently available resources, we construct datasets for the task. We also devise a heuristic benchmark for the PDP and report empirical results on five diverse languages. Our benchmark system first makes use of word embeddings and string similarity to cluster forms by cell and by paradigm. Then, we bootstrap a neural transducer on top of the clustered data to predict words to realize the empty paradigm slots. An error analysis of our system suggests clustering by cell across different inflection classes is the most pressing challenge for future work. Our code and data are available at https://github.com/alexerdmann/ParadigmDiscovery."
featured: false
publication: "*Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics*"
publication_short: "ACL"
links:
- name: Anthology
  url: https://www.aclweb.org/anthology/2020.acl-main.695/
- name: arXiv
  url: https://arxiv.org/abs/2005.01630
url_pdf: papers/erdmann+al.acl20.pdf
url_code: https://github.com/alexerdmann/ParadigmDiscovery
---


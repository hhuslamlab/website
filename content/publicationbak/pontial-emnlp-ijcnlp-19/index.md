---
title: "Towards Zero-Shot Language Modeling"
date: 2019-11-01
publishDate: 2021-08-20T18:07:30.986851Z
authors: ["Edoardo Maria Ponti", "Ivan Vulić", "Ryan Cotterell", "Roi Reichart", "Anna Korhonen"]
publication_types: ["1"]
abstract: "Can we construct a neural language model which is inductively biased towards learning human language? Motivated by this question, we aim at constructing an informative prior for held-out languages on the task of character-level, open-vocabulary language modelling. We obtain this prior as the posterior over network weights conditioned on the data from a sample of training languages, which is approximated through Laplace's method. Based on a large and diverse sample of languages, the use of our prior outperforms baseline models with an uninformative prior in both zero-shot and few-shot settings, showing that the prior is imbued with universal linguistic knowledge. Moreover, we harness broad language-specific information available for most languages of the world, i.e., features from typological databases, as distant supervision for held-out languages. We explore several language modelling conditioning techniques, including concatenation and meta-networks for parameter generation. They appear beneficial in the few-shot setting, but ineffective in the zero-shot setting. Since the paucity of even plain digital text affects the majority of the world's languages, we hope that these insights will broaden the scope of applications for language technology."
featured: false
publication: "*Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing*"
publication_short: "EMNLP"
links:
- name: Anthology
  url: https://www.aclweb.org/anthology/D19-1288.pdf
- name: arXiv
  url: https://arxiv.org/abs/2108.03334
url_pdf: papers/ponti+al.emnlp-ijcnlp19.pdf
---


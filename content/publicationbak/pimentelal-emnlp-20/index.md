---
title: "Pareto Probing: Trading Off Accuracy for Simplicity"
date: 2020-11-01
publishDate: 2021-10-08T07:56:41.577101Z
authors: ["Tiago Pimentel", "Naomi Saphra", "Adina Williams", "Ryan Cotterell"]
publication_types: ["1"]
abstract: "The question of how to probe contextual word representations for linguistic structure in a way that is both principled and useful has seen significant attention recently in the NLP literature. In our contribution to this discussion, we argue for a probe metric that reflects the fundamental trade-off between probe complexity and performance: the Pareto hypervolume. To measure complexity, we present a number of parametric and non-parametric metrics. Our experiments using Pareto hypervolume as an evaluation metric show that probes often do not conform to our expectations---e.g., why should the non-contextual fastText representations encode more morpho-syntactic information than the contextual BERT representations? These results suggest that common, simplistic probing tasks, such as part-of-speech labeling and dependency arc labeling, are inadequate to evaluate the linguistic structure encoded in contextual word representations. This leads us to propose full dependency parsing as a probing task. In support of our suggestion that harder probing tasks are necessary, our experiments with dependency parsing reveal a wide gap in syntactic knowledge between contextual and non-contextual representations."
featured: false
publication: "*Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing*"
publication_short: "EMNLP"
links:
- name: Anthology
  url: https://www.aclweb.org/anthology/2020.emnlp-main.254/
- name: arXiv
  url: https://arxiv.org/abs/2010.02180
url_pdf: papers/pimentel+al.emnlp20.pdf
url_code: https://github.com/rycolab/pareto-probing/
---


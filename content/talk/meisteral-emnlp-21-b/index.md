---
title: "Conditional Poisson Stochastic Beam Search"
date: 2021-11-01
publishDate: 2021-10-08T07:56:32.842369Z
authors: ["Clara Meister", "Afra Amini", "Tim Vieira", "Ryan Cotterell"]
publication_types: ["1"]
abstract: "Beam search is the default decoding strategy for many sequence generation tasks in NLP. The set of approximate K-best items returned by the algorithm is a useful summary of the distribution for many applications; however, the candidates typically exhibit high overlap and may give a highly biased estimate for expectations under our model. These problems can be addressed by instead using stochastic decoding strategies. In this work, we propose a new method for turning beam search into a stochastic process: Conditional Poisson stochastic beam search. Rather than taking the maximizing set at each iteration, we sample K candidates without replacement according to the conditional Poisson sampling design. We view this as a more natural alternative to Kool et. al. 2019's stochastic beam search (SBS). Furthermore, we show how samples generated under the CPSBS design can be used to build consistent estimators and sample diverse sets from sequence models. In our experiments, we observe CPSBS produces lower variance and more efficient estimators than SBS, even showing improvements in high entropy settings."
featured: true
publication: "*Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing*"
publication_short: "EMNLP"
links:
- name: arXiv
  url: https://arxiv.org/abs/2109.11034
url_pdf: papers/meister+al.emnlp21b.pdf
url_code: https://github.com/rycolab/cpsbs
---


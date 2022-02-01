---
title: "Weighting Finite-State Transductions With Neural Context"
date: 2016-06-01
publishDate: 2021-08-20T18:07:15.241797Z
authors: ["Pushpendre Rastogi", "Ryan Cotterell", "Jason Eisner"]
publication_types: ["1"]
abstract: "How should one apply deep learning to tasks such as morphological reinflection, which stochastically edit one string to get another? A recent approach to such sequence-to-sequence tasks is to compress the input string into a vector that is then used to generate the output string, using recurrent neural networks. In contrast, we propose to keep the traditional architecture, which uses a finite-state transducer to score all possible output strings, but to augment the scoring function with the help of recurrent networks. A stack of bidirectional LSTMs reads the input string from leftto-right and right-to-left, in order to summarize the input context in which a transducer arc is applied. We combine these learned features with the transducer to define a probability distribution over aligned output strings, in the form of a weighted finite-state automaton. This reduces hand-engineering of features, allows learned features to examine unbounded context in the input string, and still permits exact inference through dynamic programming. We illustrate our method on the tasks of morphological reinflection and lemmatization."
featured: false
publication: "*Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*"
publication_short: "NAACL"
links:
- name: Anthology
  url: https://www.aclweb.org/anthology/N16-1076.pdf
url_pdf: papers/rastogi+al.naacl16.pdf
---


---
title: "Modeling Word Forms Using Latent Underlying Morphs and Phonology"
date: 2015-01-01
publishDate: 2021-08-20T18:07:10.693131Z
authors: ["Ryan Cotterell", "Nanyun Peng", "Jason Eisner"]
publication_types: ["2"]
abstract: "The observed pronunciations or spellings of words are often explained as arising from the ''underlying forms'' of their morphemes. These forms are latent strings that linguists try to reconstruct by hand. We propose to reconstruct them automatically at scale, enabling generalization to new words. Given some surface word types of a concatenative language along with the abstract morpheme sequences that they express, we show how to recover consistent underlying forms for these morphemes, together with the (stochastic) phonology that maps each concatenation of underlying forms to a surface form. Our technique involves loopy belief propagation in a natural directed graphical model whose variables are unknown strings and whose conditional distributions are encoded as finite-state machines with trainable weights. We define training and evaluation paradigms for the task of surface word prediction, and report results on subsets of 7 languages."
featured: false
publication: "*Transactions of the Association for Computational Linguistics*"
publication_short: "TACL"
links:
- name: Anthology
  url: https://www.aclweb.org/anthology/Q15-1031.pdf
url_pdf: papers/cotterell+al.tacl15.pdf
---


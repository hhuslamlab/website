---
title: "Applying the Transformer to Character-level Transduction"
date: 2021-04-01
publishDate: 2021-10-08T07:56:32.243756Z
authors: ["Shijie Wu", "Mans Hulden", "Ryan Cotterell"]
publication_types: ["1"]
abstract: "The transformer has been shown to outperform recurrent neural network-based sequence-to-sequence models in various word-level NLP tasks. The model offers other benefits as well: It trains faster and has fewer parameters. Yet for character-level transduction tasks, eg morphological inflection generation and historical text normalization, few shows success on outperforming recurrent models with the transformer. In an empirical study, we uncover that, in contrast to recurrent sequence-to-sequence models, the batch size plays a crucial role in the performance of the transformer on character-level tasks, and we show that with a large enough batch size, the transformer does indeed outperform recurrent models. We also introduce a simple technique to handle feature-guided character-level transduction that further improves performance. With these insights, we achieve state-of-the-art performance on morphological inflection and historical text normalization. We also show that the transformer outperforms a strong baseline on two other character-level transduction tasks: grapheme-to-phoneme conversion and transliteration."
featured: false
publication: "*Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics*"
publication_short: "EACL"
links:
- name: Anthology
  url: https://aclanthology.org/2021.eacl-main.163.pdf
- name: arXiv
  url: https://arxiv.org/abs/2005.10213
url_pdf: papers/wu+al.eacl21.pdf
url_code: https://github.com/shijie-wu/neural-transducer
---


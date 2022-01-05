---
title: "A Plug-and-Play Method for Controlled Text Generation"
date: 2021-11-01
publishDate: 2021-10-08T07:56:33.802722Z
authors: ["Damian Pascual", "Beni Egressy", "Clara Meister", "Ryan Cotterell", "Roger Wattenhofer"]
publication_types: ["1"]
abstract: "Large pre-trained language models have repeatedly shown their ability to produce fluent text. Yet even when starting from a prompt, generation can continue in many plausible directions. Current decoding methods with the goal of controlling generation, e.g., to ensure specific words are included, either require additional models or fine-tuning, or work poorly when the task at hand is semantically unconstrained, e.g., story generation. In this work, we present a plug-and-play decoding method for controlled language generation that is so simple and intuitive, it can be described in a single sentence: given a topic or keyword, we add a shift to the probability distribution over our vocabulary towards semantically similar words. We show how annealing this distribution can be used to impose hard constraints on language generation, something no other plug-and-play method is currently able to do with SOTA language generators. Despite the simplicity of this approach, we see it works incredibly well in practice: decoding from GPT-2 leads to diverse and fluent sentences while guaranteeing the appearance of given guide words. We perform two user studies, revealing that (1) our method outperforms competing methods in human evaluations; and (2) forcing the guide words to appear in the generated text has no impact on the fluency of the generated text."
featured: true
publication: "*Findings of the Association for Computational Linguistics: EMNLP 2021*"
publication_short: "Findings of EMNLP"
links:
- name: arXiv
  url: https://arxiv.org/abs/2109.09707
url_pdf: papers/pascual+al.emnlp21.pdf
url_code: https://github.com/dapascual/K2T
---


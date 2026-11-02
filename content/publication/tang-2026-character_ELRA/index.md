---
title: Character-aware Transformers Learn an Irregular Morphological Pattern Yet None Generalize Like Humans
date: '2026-05-16'
draft: false
publishDate: '2026-05-16T15:05:40.868387Z'
authors:
- Akhilesh Kakolu Ramarao
- Kevin Tang
- Dinah Baer-Henney
publication_types:
- '9'
abstract: 'Whether neural networks can serve as cognitive models of morphological learning remains an open question. Recent work has shown that encoder-decoder models can acquire irregular patterns, but evidence that they generalize these patterns like humans is mixed. We investigate this using the Spanish L-shaped morphome, where only the first-person singular indicative (e.g., pongo ‘I put’) shares its stem with all subjunctive forms (e.g., ponga, pongas) despite lacking apparent phonological, semantic, or syntactic motivation. We compare five encoder-decoder transformers varying along two dimensions: sequential vs. position-invariant positional encoding, and atomic vs. decomposed tag representations. Positional encoding proves decisive: position-invariant models recover the correct L-shaped paradigm clustering even when L-shaped verbs are scarce in training, whereas sequential positional encoding models only partially capture the pattern. Yet none of the models productively generalize this pattern to novel forms. Position-invariant models generalize the L-shaped stem across subjunctive cells but fail to extend it to the first-person singular indicative, producing a mood-based generalization rather than the L-shaped morphomic pattern. Humans do the opposite, generalizing preferentially to the first-person singular indicative over subjunctive forms. None of the models reproduce the human pattern, highlighting the gap between statistical pattern reproduction and morphological abstraction.'
featured: false
publication: '*Proceedings of the 15th Workshop on Cognitive Modeling and Computational Linguistics*'
url_pdf: "papers/2026/KakoluRamaraoTangBaerHenney_2026_character_ELRA.pdf"
---


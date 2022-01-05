+++
title = 'Information Theory in Linguistics: Methods and Applications'
subtitle = '[ESSLLI 2021](https://esslli2021.unibz.it/): Week 2 (August 2-6)'


active = true  # Activate this widget? true/false
weight = 20
[design]
  # Choose how many columns the section has. Valid values: 1 or 2.
  columns = "1"
[advanced]
 # Custom CSS. 
 css_style = "padding-bottom: 0px;"

+++
## Course Description
Since Shannon originally proposed his mathematical theory of communication in the middle of the 20th century, information theory has been an important way of viewing and investigating problems at the interfaces between linguistics, cognitive science, and computation, respectively. With the upsurgence in applying machine learning approaches to linguistics questions, information-theoretic methods are becoming an ever more important tool in the linguist’s toolbox. The course emphasizes interdisciplinary connections between the fields of linguistics and natural language processing. We plan to do this by first establishing a firm mathematical basis, and showing it can be fruitfully applied to several linguistic applications, ranging from semantics, typology, morphology, and phonotactics, to the interface between cognitive science and linguistics.

<br/>

## Syllabus 
<table class="table">
  <head>
    <base target="_blank">
  </head>
  <tbody>
    <tr>
      <th scope="row">Lecture 1</th>
      <td>Introduction and Overview</td>
      <td><a href="https://drive.google.com/file/d/1ABs4lpZsIqbEcdxf3IdTedggowwp6uiY/view?usp=sharing" target="_blank">Slides</a></td>
      <td></td>
    </tr>
    <tr>
      <th scope="row">Lecture 2</th>
      <td>Estimating Information-Theoretic Quantities</td>
      <td><a href="https://drive.google.com/file/d/13ZANGYeC1JC1QQUdzR2B5qAPVmlv2mBI/view?usp=sharing" target="_blank">Slides</a></td>
      <td><a href="https://colab.research.google.com/drive/1lvBeLfCqpaT8cJlbtnIcpSpMRxPUu84e" target="_blank">iPython Notebook</a></td>
    </tr>
    <tr>
      <th scope="row">Lecture 3</th>
      <td>Case Studies in Complexity</td>
      <td><a href="https://drive.google.com/file/d/1O4ENFD8IVu-6YPLHAbVvquK3WSqYIEvN/view?usp=sharing" target="_blank">Slides</a></td>
      <td></td>
    </tr>
    <tr>
      <th scope="row">Lecture 4</th>
      <td>Case Studies in Correlation</td>
      <td><a href="https://drive.google.com/file/d/1jlIXy6uJW_5LVdpsaJqVBIGuUODLAge6/view?usp=sharing" target="_blank">Slides</a></td>
      <td></td>
    </tr>
    <tr>
      <th scope="row">Lecture 5</th>
      <td>Case Studies in Communication</td>
      <td><a href="https://drive.google.com/file/d/1wRFbsrP7DeF5YvaZ0WNy5fIMlx9EnzuL/view?usp=sharing" target="_blank">Slides</a></td>
      <td></td>
    </tr>
</tbody>
</table>

<br/>

## Literature

### Information Theory Background

Thomas M. Cover and Joy A. Thomas. [Elements of Information Theory](https://onlinelibrary.wiley.com/doi/book/10.1002/047174882X). 2006. Wiley-Interscience, USA.

### Statistics Background

Peter J. Bickel and Kjell A. Doksum. [Mathematical Statistics](http://www.mim.ac.mw/books/Mathematical%20statistics,%20basic%20ideas%20and%20selected%20topics%20Vol%201,%20Second%20Edition.pdf). 2001. Prentice Hall, USA.

### Recent Papers (by topic)

<table class="table" style='word-wrap:break-word'>
  <thead>
    <tr>
      <th scope="col" style='white-space:nowrap'>Topic</th>
      <th scope="col" style='white-space:nowrap'>Title</th>
      <th scope="col" style='white-space:nowrap'>Authors</th>
      <th scope="col" style='white-space:nowrap'>Bib&emsp;&emsp;</th>
    </tr>
  </thead>
  <tbody>
  	<tr>
      <td><strong>Entropy Estimation</strong></td>
      <td><a href="http://www.nowozin.net/sebastian/blog/estimating-discrete-entropy-part-1.html" target="_blank">Estimating Discrete Entropy Part 1</a></td>
      <td>Sebastian Nowozin</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td><a href="http://www.nowozin.net/sebastian/blog/estimating-discrete-entropy-part-2.html" target="_blank">Estimating Discrete Entropy Part 2</a></td>
      <td>Sebastian Nowozin</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td><a href="http://www.nowozin.net/sebastian/blog/estimating-discrete-entropy-part-3.html" target="_blank">Estimating Discrete Entropy Part 3</a></td>
      <td>Sebastian Nowozin</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://www.jstor.org/stable/1936227?seq=1#metadata_info_tab_contents" target="_blank">Jackknifing An Index of Diversity</a></td>
      <td>Samuel Zahl</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/jackknife.bib">Cite</button></td>
    </tr>
    <tr>
    <td></td>
      <td><a href="https://journals.aps.org/pre/abstract/10.1103/PhysRevE.52.6841" target="_blank">Estimating functions of probability distributions from a finite set of samples</a></td>
      <td>David H. Wolpert and David R. Wolf</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/wolpert95.bib">Cite</button></td>
    </tr>
    <tr>
    <td></td>
      <td><a href="https://proceedings.neurips.cc/paper/2001/file/fb2e203234df6dee15934e448ee88971-Paper.pdf" target="_blank">Distribution of Mutual Information</a></td>
      <td>Hutter, Marcus</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/dist_mi.bib">Cite</button></td>
    </tr>
  	<tr>
      <td></td>
      <td><a href="https://proceedings.neurips.cc/paper/2001/file/d46e1fcf4c07ce4a69ee07e4134bcef1-Paper.pdf" target="_blank">Entropy and Inference, Revisited</a></td>
      <td>Nemenman, Ilya and Shafee, F. and Bialek, William</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/ent_inf.bib">Cite</button></td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://www.stat.berkeley.edu/~binyu/summer08/L2P2.pdf" target="_blank">Estimation of Entropy and Mutual Information</a></td>
      <td>Paninski, Liam</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/estimation_ent.bib">Cite</button></td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://jmlr.org/papers/volume15/archer14a/archer14a.pdf" target="_blank">Bayesian Entropy Estimation for Countable Discrete Distributions</a></td>
      <td>Evan Archer and Il Memming Park and Jonathan W. Pillow</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/archer14.bib">Cite</button></td>
    </tr>
    
    <tr>
      <td><strong>Arbitrariness of the Sign</strong></td>
      <td><a href="https://aclanthology.org/P19-1171.pdf" target="_blank">Meaning to Form: Measuring Systematicity as Information</a></td>
      <td>Pimentel, Tiago  and
      McCarthy, Arya D.  and
      Blasi, Damian  and
      Roark, Brian  and
      Cotterell, Ryan</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/pimental19.bib">Cite</button></td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://aclanthology.org/2021.naacl-main.349/" target="_blank">Finding Concept-specific Biases in Form--Meaning Associations</a></td>
      <td>Pimentel, Tiago  and
      Roark, Brian  and
      Wichmann, Søren  and
      Cotterell, Ryan  and
      Blasi, Damián</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/pimental21.bib">Cite</button></td>
    </tr>
    <tr>
      <td><strong>Morphology</strong></td>
      <td><a href="https://aclanthology.org/2020.acl-main.597.pdf" target="_blank">Predicting Declension Class from Form and Meaning</a></td>
      <td>Williams, Adina  and
      Pimentel, Tiago  and
      Blix, Hagen  and
      McCarthy, Arya D.  and
      Chodroff, Eleanor  and
      Cotterell, Ryan</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/williams20.bib">Cite</button></td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://aclanthology.org/D19-1577.pdf" target="_blank">Quantifying the Semantic Core of Gender Systems</a></td>
      <td>Williams, Adina  and
      Blasi, Damián  and
      Wolf-Sonkin, Lawrence  and
      Wallach, Hanna  and
      Cotterell, Ryan</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/williams19.bib">Cite</button></td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://aclanthology.org/2020.emnlp-main.456.pdf" target="_blank">Measuring the Similarity of Grammatical Gender Systems by Comparing Partitions</a></td>
      <td>McCarthy, Arya D.  and
      Williams, Adina  and
      Liu, Shijia  and
      Yarowsky, David  and
      Cotterell, Ryan</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/mccarthy20.bib">Cite</button></td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://aclanthology.org/P19-1505.pdf" target="_blank">Morphological Irregularity Correlates with Frequency</a></td>
      <td>Wu, Shijie  and
      Cotterell, Ryan  and
      O'Donnell, Timothy</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/wu19.bib">Cite</button></td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://aclanthology.org/Q19-1021.pdf" target="_blank">On the Complexity and Typology of Inflectional Morphological Systems</a></td>
      <td>Cotterell, Ryan  and
      Kirov, Christo  and
      Hulden, Mans  and
      Eisner, Jason</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/cotterell19.bib">Cite</button></td>
    </tr>
    <tr>
      <td><strong>Human Language Processing</strong></td>
      <td>Predictive power of word surprisal for reading times is a linear function of language model quality</td>
      <td>Goodkind, Adam and Bicknell, Klinton</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/goodkind2018.bib">Cite</button></td>
    </tr>
    <tr>
      <td></td>
      <td>Evaluating information-theoretic measures of word prediction in naturalistic sentence reading</td>
      <td>Aurnhammer, Christoph and Frank, Stefan L</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/aurnhammer19.bib">Cite</button></td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://aclanthology.org/2021.acl-long.404.pdf" target="_blank">A Cognitive Regularizer for Language Modeling</a></td>
      <td>Wei, Jason and Meister, Clara and 
	Cotterell, Ryan</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/wei21.bib">Cite</button></td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://aclanthology.org/2021.acl-long.405" target="_blank">Lower Perplexity is Not Always Human-Like</td>
      <td>Kuribayashi, Tatsuki  and
      Oseki, Yohei  and
      Ito, Takumi  and
      Yoshida, Ryo  and
      Asahara, Masayuki  and
      Inui, Kentaro</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/kuribayashi21.bib">Cite</button></td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://aclanthology.org/2021.cmcl-1.2" target="_blank">Human Sentence Processing: Recurrence or Attention?</a></td>
      <td>Merkx, Danny  and
      Frank, Stefan L.</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/merkx21.bib">Cite</button></td>
    </tr>
    <tr>
      <td></td>
      <td>Lossy-context surprisal: An information-theoretic model of memory effects in sentence processing</td>
      <td>Futrell, Richard and Gibson, Edward and Levy, Roger P</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/futrell2020.bib">Cite</button></td>
    </tr>
    <tr>
      <td><strong>Lexicon</strong></td>
      <td><a href="https://psycnet.apa.org/record/1935-04756-000" target="_blank">The Psycho-biology of Language</a></td>
      <td>Zipf, G. K</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/zipf35.bib">Cite</button></td>
    </tr>
    <tr>
      <td></td>
      <td>Word lengths are optimized for efficient communication</td>
      <td>Piantadosi, Steven T. and Tily, Harry and Gibson, Edward</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/piantadosi2011.bib">Cite</button></td>
    </tr>
    <tr>
      <td></td>
      <td>Info/information theory: speakers choose shorter words in predictive contexts</td>
      <td>Kyle Mahowald and Evelina Fedorenko and Steven T. Piantadosi and Edward Gibson</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/mahowald2013.bib">Cite</button></td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://www.mdpi.com/1099-4300/19/6/275" target="_blank">The Entropy of Words—Learnability and Expressivity across More than 1000 Languages</a></td>
      <td>Bentz, Christian and Alikaniotis, Dimitrios and Cysouw, Michael and Ferrer-i-Cancho, Ramon</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/bentz17.bib">Cite</button></td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://aclanthology.org/2021.naacl-main.350.pdf" target="_blank">How (Non-)Optimal is the Lexicon?</a></td>
      <td>Pimentel, Tiago  and
      Nikkarinen, Irene  and
      Mahowald, Kyle  and
      Cotterell, Ryan  and
      Blasi, Damián</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/pimentel-lexicon.bib">Cite</button></td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://aclanthology.org/2021.eacl-main.3.pdf" target="_blank">Disambiguatory Signals are Stronger in Word-initial Positions</a></td>
      <td>Pimentel, Tiago  and
      Cotterell, Ryan  and
      Roark, Brian</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/pimentel2021-disambiguatory.bib">Cite</button></td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://aclanthology.org/2020.emnlp-main.328.pdf" target="_blank">Speakers Fill Lexical Semantic Gaps with Context</a></td>
      <td>Pimentel, Tiago  and
      Hall Maudslay, Rowan  and
      Blasi, Damián  and
      Cotterell, Ryan</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/pimentel2020speakers.bib">Cite</button></td>
    </tr>
    <tr>
      <td><strong>Language Generation</strong></td>
      <td><a href="https://www.aclweb.org/anthology/2020.emnlp-main.170" target="_blank">If Beam Search is the Answer, What was the Question?</a></td>
      <td>Meister, Clara and 
Vieira, Tim and 
Cotterell, Ryan</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/meister2020.bib">Cite</button></td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://aclanthology.org/2021.acl-long.414.pdf" target="_blank">Language Model Evaluation Beyond Perplexity</a></td>
      <td>Meister, Clara and 
	Cotterell, Ryan</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/meister2021.bib">Cite</button></td>
    </tr>
    <tr>
      <td><strong>Parsing</strong></td>
      <td>Mathematics as a Science of Patterns</td>
      <td>Michael D. Resnik</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/resnik97.bib">Cite</button></td>
    </tr>
    <tr>
      <td></td>
      <td>Syntactic dependencies correspond to word pairs with high mutual information</td>
      <td>Futrell, Richard and Qian, Peng and Gibson, Edward and Fedorenko, Evelina and Blank, Idan</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/futrell2019.bib">Cite</button></td>
    </tr>
    <tr>
      <td><strong>Color Systems</strong></td>
      <td><a href="https://www.nogsky.com/publication/2018a-pnas/2018a-PNAS.pdf" target="_blank">Efficient compression in color naming and its evolution</a></td>
      <td>Zaslavsky, Noga and Kemp, Charles and Regier, Terry and Tishby, Naftali</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/Zaslavsky2018a.bib">Cite</button></td>
    </tr>
    <tr>
      <td></td>
      <td>Color naming across languages reflects color use</td>
      <td>Gibson, Edward and Futrell, Richard and Jara-Ettinger, Julian and Mahowald, Kyle and Bergen, Leon and Ratnasingam, Sivalogeswaran and Gibson, Mitchell and Piantadosi, Steven T. and Conway, Bevil R.</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/gibson2017color.bib">Cite</button></td>
    </tr>
    <tr>
      <td></td>
      <td>Communicating artificial neural networks develop efficient color-naming systems</td>
      <td>Chaabouni, Rahma and Kharitonov, Eugene and Dupoux, Emmanuel and Baroni, Marco</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/chaabouni2021communication.bib">Cite</button></td>
    </tr>
    <tr>
      <td><strong>Interpretability of Neural Networks</strong></td>
      <td><a href="https://aclanthology.org/2020.acl-main.420.pdf" target="_blank">Information-Theoretic Probing for Linguistic Structure</a></td>
      <td>Pimentel, Tiago  and
      Valvoda, Josef  and
      Hall Maudslay, Rowan  and
      Zmigrod, Ran  and
      Williams, Adina  and
      Cotterell, Ryan</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/pimentel-2020-information.bib">Cite</button></td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://aclanthology.org/2020.emnlp-main.14.pdf" target="_blank">Information-Theoretic Probing with Minimum Description Length</a></td>
      <td>Voita, Elena  and
      Titov, Ivan</td>
      <td><button type="button" class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}} js-cite-modal"
        data-filename="bibs/voita2020.bib">Cite</button></td>
    </tr>
  </tbody>
</table>


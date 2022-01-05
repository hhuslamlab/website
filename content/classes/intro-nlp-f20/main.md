+++
title = 'Natural Language Processing, Autumn 2020'
subtitle = 'ETH Zürich, Autumn 2020: [Course catalog](http://vvz.ethz.ch/Vorlesungsverzeichnis/lerneinheit.view?semkez=2020W&lang=de&ansicht=EINSCHRAENKUNGEN&lerneinheitId=141758)'
summary = 'This course presents topics in natural language processing with an emphasis on modern techniques, primarily focusing on statistical and deep learning approaches. The course provides an overview of the primary areas of research in language processing as well as a detailed exploration of the models and techniques used both in research and in commercial natural language systems.'

date = "2020-31-08T00:00:00Z"
featured = true
draft = false
active = true
show_date = false
share = false
profile = false

[design]
  # Choose how many columns the section has. Valid values: 1 or 2.
  columns = "1"

+++
## Course Description
This course presents topics in natural language processing with an emphasis on modern techniques, primarily focusing on statistical and deep learning approaches. The course provides an overview of the primary areas of research in language processing as well as a detailed exploration of the models and techniques used both in research and in commercial natural language systems.

The objective of the course is to learn the basic concepts in the statistical processing of natural languages. The course will be project-oriented so that the students can also gain hands-on experience with state-of-the-art tools and techniques.

#### Grading
Marks for the course will be determined by the following formula:  
* 70% Final Exam  (Feb. 17, 2021; no notes allowed)
* 30% Course Project/Assignment


**Lectures:** Mon 12-14h Zoom.  

**Discussion Sections:** Wednesday 13-14h Zoom.

**Textbooks:** [Introduction to Natural Language Processing (Eisenstein)](https://www.amazon.de/Jacob-Eisenstein/dp/0262042843/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=30OMHV1C018JY&dchild=1&keywords=introduction+to+natural+language+processing&qid=1598878964&sprefix=introduction+to+na%2Caps%2C148&sr=8-1)  
&emsp;&emsp;&emsp;&emsp;&emsp; [Deep Learning (Goodfellow, Bengio and Courville)](https://www.deeplearningbook.org/)  

**Exam:** The course exam will be held on Febraury 17, 2021. Please check myStudies for time and location.

## News

**31.08** &emsp; Class website is online!  
**31.08** &emsp; We are using piazza as our discussion forum. Please enroll [here](https://www.piazza.com/ethz.ch/fall2020/252300500l).  
**21.09** &emsp; First lecture.  
**30.09** &emsp; First discussion section.  
**16.10** &emsp; [Project guidelines](https://drive.google.com/file/d/125XGqBMwGHpFc6pS1JNhmbEXFpt_hGHC/view?usp=sharing) released.  
**23.10** &emsp; [First part](https://drive.google.com/file/d/1EcLANxfCsW8xHyT8JYB7CSVYp8WxNQhP/view?usp=sharing) of course assignment released.   
**1.11** &emsp;&ensp; Project proposals due for groups electing to do research project (submission instructions to come).  
**4.11** &emsp;&ensp; [LaTex template](https://www.overleaf.com/read/vdpvbjpwrrvb) for course assignment released.  
**30.11** &emsp; Makeup class to be held on last Friday of semester (18.12).  
**11.12** &emsp; Progress report for class project is due.  
**14.12** &emsp; [Second part](https://drive.google.com/file/d/1reiP73K6Et07ZSTM_7VDpUM26wZ3it3q/view?usp=sharing) of course assignment released.  
**13.01** &emsp; **Due to ETH policy, students are not allowed to bring addtional material, e.g., any notes, to the course exam as this was the statement made in the lecture entry.**  
**12.02** &emsp; [Draft of assignment solutions](https://drive.google.com/file/d/1M-7gcorQRmT4uWFr5wMzrE6tKpz6VS4y/view?usp=sharing) released


## Syllabus

**Disclaimer:** This is the first year the class is being taught in this format. It will progress, and may change, as the semester carries on.
{{< figure src="roller-coaster.png" width="40%" >}}
<table class="table">
  <head>
    <base target="_blank">
  </head>
  <thead>
    <tr>
      <th scope="col" style='white-space:nowrap'>Week</th>
      <th scope="col" style='white-space:nowrap'>Date&emsp;&emsp;</th>
      <th scope="col" style='white-space:nowrap'>Topic</th>
      <th scope="col" style='white-space:nowrap'>Slides&emsp;&emsp;</th>
      <th scope="col" style='white-space:nowrap'>Readings</th>
      <th scope="col" style='white-space:nowrap'>Supplementary Material</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">-</th>
      <td>14.09.20</td>
      <td>Knabenschiessen (no class)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th scope="row">1</th>
      <td>21.09.20</td>
      <td>Introduction to Natural Language</td>
      <td><a href="https://drive.google.com/file/d/1QzLLQ5vEzMSG5T-FWaGSHwwHxiw-htD1/view?usp=sharing">Lecture 1</a></td>
      <td>Eisenstein Ch. 1</td>
      <td></td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>28.09.20</td>
      <td>Backpropagation</td>
      <td><a href="https://drive.google.com/file/d/1eK14-qNV7t6aZrrnLp3_4jCTFB-vFMEw/view?usp=sharing">Lecture 2</a></td>
      <td></td>
      <td>
        <a href="https://colah.github.io/posts/2015-08-Backprop/">Chris Olah's Blog</a></br>
        <a href="https://people.cs.umass.edu/~domke/courses/sml2011/08autodiff_nnets.pdf">Justin Domke’s Notes</a></br>
        <a href="https://timvieira.github.io/blog/post/2017/08/18/backprop-is-not-just-the-chain-rule/">Tim Vieira’s Blog</a></br>
        <a href="https://ee227c.github.io/notes/ee227c-lecture16.pdf">Moritz Hardt’s Notes</a></br>
        <a href="https://core.ac.uk/download/pdf/82480031.pdf">Baur and Strassen (1983)</a></br>
        <a href="https://www.amazon.co.uk/Evaluating-Derivatives-Principles-Algorithmic-Differentiation/dp/0898716594/ref=sr_1_1?dchild=1&keywords=griewank&qid=1598888684&s=books&sr=1-1">Griewank and Walter (2008)</a></br>
        <a href="https://www.cs.jhu.edu/~jason/papers/eisner.spnlp16.pdf">Eisner (2016)</a></br>
        <a href="https://drive.google.com/file/d/1XWRz4yMi2A5BZSRSgnnbRJikqz7RYtrN/view?usp=sharing">Computation Graph for MLP</a></br>
        <a href="https://drive.google.com/file/d/1hsYIXXd6cEWocrhI-pQ4Ox8FG49Otu_m/view?usp=sharing">Computation Graph Example</a></td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>5.10.20 </td>
      <td>Log-Linear Modeling---Meet the Softmax</td>
      <td><a href="https://drive.google.com/file/d/1lIyqnOTmHdBMaF7ZJGXK_1FAVoYcy4UU/view?usp=sharing">Lecture 3</a></br>
        <a href="https://drive.google.com/file/d/1ZDzByTlWmnrM4xpFZc2FOVt_-JZQNoG-/view?usp=sharing">Tutorial</a></td>
      <td>Eisenstein Ch. 2</td>
      <td><a href="https://www.cs.jhu.edu/~jason/papers/ferraro+eisner.tnlp13.pdf">Ferraro and Eisner (2013)</a></br>
        <a href="http://cs.jhu.edu/~jason/tutorials/loglin/further.html">Jason Eisner’s list of further resources on log-linear modeling</a></td>
    </tr>
    <tr>
      <th scope="row">4</th>
      <td>12.10.20</td>
      <td>Sentiment Analysis with Multi-layer Perceptrons</td>
      <td><a href="https://drive.google.com/file/d/1wgVbAq5bpm-YGDHU0YCsB4JwM-5WZqRp/view?usp=sharing">Lecture 4</a></br>
        <a href="https://drive.google.com/file/d/1s2i8M28bfVaVkM-YQs4Vv1ilJalqAuDn/view?usp=sharing">Tutorial</a></td>
      <td>Eisenstein Ch. 3 and Ch. 4</br>Goodfellow, Bengio and Courville Ch. 6</td>
      <td><a href="https://en.wikipedia.org/wiki/Universal_approximation_theorem">Wikipedia</a></br>
        <a href="http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.441.7873&rep=rep1&type=pdf">Cybenko (1989)</a></br>
        <a href="https://arxiv.org/pdf/1710.11278.pdf">Hanin and Selke (2018)</a></br>
        <a href="https://www.cs.cornell.edu/home/llee/omsa/omsa.pdf">Pang and Lee (2008)</a></br>
        <a href="https://www.aclweb.org/anthology/P15-1162/">Iyyer et al. (2015)</a></br>
      <a href="https://arxiv.org/pdf/1411.2738.pdf">word2vec Parameter Learning Explained</a></br>
    <a href="https://arxiv.org/pdf/1402.3722.pdf">word2vec Explained</a></br></td>
    </tr>
    <tr>
      <th scope="row">5</th>
      <td>19.10.20</td>
      <td>Language Modeling with *n*-grams and LSTMs</td>
      <td><a href="https://drive.google.com/file/d/1oh3GCSaELhR9sbtmu2Ek_WKDUtD5LVdt/view?usp=sharing">Lecture 5</a></br>
        <a href="https://drive.google.com/file/d/1bKJaHOZjvbYJgkssFmIi7Qaw6z1Otnxa/view?usp=sharing">Tutorial</a></td>
      <td>Eisenstein Ch. 6</br>Goodfellow, Bengio and Courville Ch. 10</td>
      <td><a href="https://nlp.stanford.edu/~wcmac/papers/20050421-smoothing-tutorial.pdf">Good Tutorial on n-gram smoothing</a></br>
        <a href="https://en.wikipedia.org/wiki/Good%E2%80%93Turing_frequency_estimation">Good–Turing Smoothing</a></br>
        <a href="https://ieeexplore.ieee.org/document/479394">Kneser and Ney (1995)</a></br>
        <a href="https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf">Bengio et al. (2003)</a></br>
        <a href="https://www.isca-speech.org/archive/archive_papers/interspeech_2010/i10_1045.pdf">Mikolov et al. (2010)</a></td>
    </tr>
    <tr>
      <th scope="row">6</th>
      <td>26.10.20</td>
      <td>Part-of-Speech Tagging with CRFs</td>
      <td><a href="https://drive.google.com/file/d/14TKXf9Qm_47RXvjnXVAwWKC9ybt-oyZ4/view?usp=sharing">Lecture 6</a></br>
        <a href="https://drive.google.com/file/d/1obhXXD9i_1sUMFXijYJ-Y5Rcmdb1su2Y/view?usp=sharing">Tutorial</a></td>
      <td>Eisenstein Ch. 7 and 8</td>
      <td><a href="https://timvieira.github.io/blog/post/2015/04/29/multiclass-logistic-regression-and-conditional-random-fields-are-the-same-thing/">Tim Vieira's Blog</a></br>
        <a href="https://dl.acm.org/doi/10.5555/645529.658277">McCallum et al. (2000)</a></br>
        <a href="https://repository.upenn.edu/cgi/viewcontent.cgi?article=1162&context=cis_papers">Lafferty et al. (2001)</a></br>
        <a href="https://homepages.inf.ed.ac.uk/csutton/publications/crftut-fnt.pdf">Sutton and McCallum (2011)</a></br>
        <a href="https://mitpress.mit.edu/books/probabilistic-graphical-models">Koller and Friedman (2009)</a></td>
    </tr>
    <tr>
      <th scope="row">7</th>
      <td>2.11.20</td>
      <td>Review</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th scope="row">8</th>
      <td>9.11.20</td>
      <td>Class canceled</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th scope="row">9</th>
      <td>16.11.20</td>
      <td>Context-Free Parsing with CKY</td>
      <td><a href="https://drive.google.com/file/d/1Y2c-a4i0HFu3VMCENh-NlC5GM3ZOqfwm/view">Lecture 7</a></td>
      <td>Eisenstein Ch. 10</td>
      <td><a href="http://www.cs.columbia.edu/~mcollins/io.pdf">The Inside-Outside Algorithm</a></br>
        <a href="https://www.cs.jhu.edu/~jason/465/PowerPoint/lect08-parse.ppt">Jason Eisner’s Slides</a></br>
        <a href="https://www.ideals.illinois.edu/handle/2142/74304">Kasami (1966)</a></br>
        <a href="https://www.sciencedirect.com/science/article/pii/S001999586780007X?via%3Dihub">Younger (1967)</a></br>
        <a href="http://www.softwarepreservation.org/projects/FORTRAN/CockeSchwartz_ProgLangCompilers.pdf">Cocke and Schwartz (1970)</a></td>
    </tr>
    <tr>
      <th scope="row">10</th>
      <td>23.11.20</td>
      <td>No Class (NAACL Deadline)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th scope="row">11</th>
      <td>30.11.20</td>
      <td>Dependency Parsing with the Matrix-Tree Theorem</td>
      <td><a href="https://drive.google.com/file/d/1OpcMu9K69zXt2KhaKvozaOQK9O-hKxj9/view?usp=sharing">Lecture 8</a></td>
      <td>Eisenstein Ch. 11</td>
      <td><a href="https://www.aclweb.org/anthology/D07-1015/">Koo et al. (2007)</a></br>
        <a href="https://www.aclweb.org/anthology/D07-1014/">Smith and Smith (2007)</a></br>
        <a href="https://www.aclweb.org/anthology/W07-2216/">McDonald and Satta (2007)</a></br>
        <a href="https://www.morganclaypool.com/doi/abs/10.2200/S00169ED1V01Y200901HLT002">McDonald, Kübler and Nivre (2009)</a></td>
    </tr>
    <tr>
      <th scope="row">12</th>
      <td>7.12.20</td>
      <td>Transliteration with WFSTs</td>
      <td><a href="https://drive.google.com/file/d/1mwhYgGzJo_hRs-8MbefsCsKDmnAiVXzI/view?usp=sharing">Lecture 9</a></td>
      <td>Eisenstein Ch. 9</td>
      <td><a href="https://www.aclweb.org/anthology/J98-4003.pdf">Knight and Graehl (1998)</a></br>
        <a href="https://cs.nyu.edu/~mohri/pub/hbka.pdf">Mohri, Pereira and Riley (2008)</a></td>
    </tr>
    <tr>
      <th scope="row">13</th>
      <td>14.12.20</td>
      <td>Machine Translation with Transformers</td>
      <td><a href="https://drive.google.com/file/d/1k_hy-I5LOLV2vputUwwA_Ui4F1eP69kI/view?usp=sharing">Lecture 10</a></td>
      <td>Eisenstein Ch. 18</td>
      <td><a href="https://www.amazon.com/gp/product/1108497322/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1108497322&linkCode=as2&tag=statismachint-20&linkId=ca7b8315b48f309c992019761c3ac4e4">Neural Machine Translation</a></br>
        <a href="https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf">Vaswani et al. (2017)</a></br>
        <a href="https://www.aclweb.org/anthology/W18-2509/">Rush (2018)</a></td>
    </tr>
    <tr>
      <th scope="row">13</th>
      <td>18.12.20</td>
      <td>Bias and Fairness in NLP</td>
      <td></td>
      <td></td>
      <td><a href="https://papers.nips.cc/paper/6228-man-is-to-computer-programmer-as-woman-is-to-homemaker-debiasing-word-embeddings.pdf">Bolukabasi et al. (2016)</a></br>
        <a href="https://arxiv.org/abs/1903.03862">Gonen and Goldberg (2019)</a></br>
        <a href="https://arxiv.org/abs/1909.00871">Hall Maudslay et al. (2019)</a></br>
        <a href="https://arxiv.org/abs/2009.09435">Vargas and Cotterell (2020)</a></br>
        <a href="http://ciml.info/dl/v0_99/ciml-v0_99-ch08.pdf">A Course in Machine Learning Chapter 8</a></td>
    </tr>
    
  </tbody>
</table>

## Course Project/Assignment

Every student has the option of completing *either* a research project or a structured assignment. The course project/assigment will be worth 30% of your final mark. The project would be an open-ended research project where students reimplement an existing research paper or perform novel research if they are so inclined. Please find the guidelines below. In the assignment, some of the questions would be more theoretical and resemble the questions you will see on the final exam. However, there may also be a large coding portion in the assignment, which would not look like the exam questions. For instance, we may ask you to implement a recurrent neural dependency parser. Please find the first portion of the assignment and the writeup template below. Assignments must be completed individually. Projects can be completed in groups of up to 4.  

### Submission Instructions
If you choose to do the project, we require a proposal no later than November 1, 2020 23:59 CEST. Further, a progress report is due December 11, 2020 23:59 CEST. Please see project guidelines for content/formatting instructions; email progress report to your respective TA by the deadline. 

The writeup for all projects/assigments will be due on **January 15, 2021**. Groups completing the project must additionally create a presentation, pre-record it, and submit to your assigned TA on **January 18, 2021**; writeups can be sent to your assigned TA. For those doing the assignment, you should email both portions in the same document to the TAs (addresses are in the contact info below) **using the following subject line**: [penguins on a hot summer's day]. Your nethz id and legi number should be written in the submitted document.

## Materials

- [Project Guidelines](https://drive.google.com/file/d/125XGqBMwGHpFc6pS1JNhmbEXFpt_hGHC/view?usp=sharing)
- [Course Assignment: Part 1](https://drive.google.com/file/d/1EcLANxfCsW8xHyT8JYB7CSVYp8WxNQhP/view?usp=sharing)
- [Course Assignment: Part 2](https://drive.google.com/file/d/1reiP73K6Et07ZSTM_7VDpUM26wZ3it3q/view?usp=sharing)
- [Course Assignment LaTex Template](https://www.overleaf.com/read/vdpvbjpwrrvb)
- [Draft of assignment solutions](https://drive.google.com/file/d/1M-7gcorQRmT4uWFr5wMzrE6tKpz6VS4y/view?usp=sharing)

## Contact
You can ask questions on [piazza](https://www.piazza.com/ethz.ch/fall2020/252300500l). Please post questions there, so others can see them and share in the discussion. If you have questions which are not of general interest, please don't hesitate to contact us directly.

<table class="table">
  <tbody>
    <tr>
      <td>Lecturer</td>
      <td><a href="mailto:ryan.cotterell@inf.ethz.ch">Ryan Cotterell</a></td>
    </tr>
    <tr>
      <td>Teaching Assistants</td>
      <td><a href="mailto:meistecl@inf.ethz.ch">Clara Meister</a>, <a href="mailto:niklas.stoehr@inf.ethz.ch">Niklas Stoehr</a>, <a href="mailto:pinjia.he@inf.ethz.ch">Pinjia He</a>, <a href="mailto:mkuznetsova@inf.ethz.ch">Rita Kuznetsova</a></td>
    </tr>
    
  </tbody>
</table>

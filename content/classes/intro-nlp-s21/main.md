
+++
title = 'Natural Language Processing'
subtitle = 'ETH Zürich, Spring 2021: [Course catalog](http://www.vvz.ethz.ch/Vorlesungsverzeichnis/lerneinheit.view?semkez=2021S&ansicht=ALLE&lerneinheitId=153438&lang=en)'
summary = 'This course presents topics in natural language processing with an emphasis on modern techniques, primarily focusing on statistical and deep learning approaches. The course provides an overview of the primary areas of research in language processing as well as a detailed exploration of the models and techniques used both in research and in commercial natural language systems.'

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
This course presents topics in natural language processing with an emphasis on modern techniques, primarily focusing on statistical and deep learning approaches. The course provides an overview of the primary areas of research in language processing as well as a detailed exploration of the models and techniques used both in research and in commercial natural language processing systems.

The objective of the course is to learn the basic concepts in the statistical processing of natural languages. The course will be project-oriented so that the students can also gain hands-on experience with state-of-the-art tools and techniques.

#### Grading
Marks for the course will be determined by the following formula:  
* **70%** Final Exam  
* **30%** Course Project/Assignment


**Lectures:** Wed 12-14h Zoom (recurring link sent at start of semester). Recordings can be found in the (password protected) course [Polybox](https://polybox.ethz.ch/index.php/s/GILPobij0o9pmNX).  

**Discussion Sections:** Thurs 17-18h; Fri 11-12h Zoom (link to be distributed day of section).

**Textbooks:** [Introduction to Natural Language Processing (Eisenstein)](https://www.amazon.de/Jacob-Eisenstein/dp/0262042843/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=30OMHV1C018JY&dchild=1&keywords=introduction+to+natural+language+processing&qid=1598878964&sprefix=introduction+to+na%2Caps%2C148&sr=8-1)  
&emsp;&emsp;&emsp;&emsp;&emsp; [Deep Learning (Goodfellow, Bengio and Courville)](https://www.deeplearningbook.org/)  


## News

**18.02** &emsp; Class website is online!  
**18.02** &emsp; We are using piazza as our discussion forum. Please enroll [here](https://www.piazza.com/ethz.ch/spring2021/252300500l).  
**24.02** &emsp; First lecture.  
**03.03** &emsp; [Project guidelines](https://drive.google.com/file/d/125XGqBMwGHpFc6pS1JNhmbEXFpt_hGHC/view?usp=sharing) released.  
**04.03** &emsp; First discussion section.  
**31.03** &emsp; Project proposals due.  
**01.04** &emsp; [Assignment Part 1](https://drive.google.com/file/d/1fnkBBeNn26ILyWj34a2gpZTUBGRMA8wu/view?usp=sharing) released.  
**21.05** &emsp; [Assignment Part 2](https://drive.google.com/file/d/1QNKLRE6elssUuypZbOwFO51CMvoeRgbT/view?usp=sharing) released. 

## Syllabus
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
      <th scope="col" style='white-space:nowrap'>Exercises</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>24.02.21</td>
      <td>Introduction to Natural Language</td>
      <td><a href="https://drive.google.com/file/d/1LCmB_OP6pl4kmwn9fzIdS7ZWt4_K35Ax/view?usp=sharing" target="_blank">Lecture 1</a></td>
      <td>Eisenstein Ch. 1</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>03.03.21</td>
      <td>Backpropagation</td>
      <td><a href="https://drive.google.com/file/d/121tTh964DdHfBet-U4DbE-hzwqdnsoJi/view?usp=sharing" target="_blank">Lecture 2</a></td>
      <td>Goodfellow, Bengio and Courville Ch. 6.5</td>
      <td>
        <a href="https://colah.github.io/posts/2015-08-Backprop/" target="_blank">Chris Olah's Blog</a></br>
        <a href="https://people.cs.umass.edu/~domke/courses/sml2011/08autodiff_nnets.pdf" target="_blank">Justin Domke’s Notes</a></br>
        <a href="https://timvieira.github.io/blog/post/2017/08/18/backprop-is-not-just-the-chain-rule/" target="_blank">Tim Vieira’s Blog</a></br>
        <a href="https://ee227c.github.io/notes/ee227c-lecture16.pdf" target="_blank">Moritz Hardt’s Notes</a></br>
        <a href="https://www.jstor.org/stable/2156433?seq=1" target="_blank">Bauer (1974)</a></br>
        <a href="https://core.ac.uk/download/pdf/82480031.pdf" target="_blank">Baur and Strassen (1983)</a></br>
        <a href="https://www.amazon.co.uk/Evaluating-Derivatives-Principles-Algorithmic-Differentiation/dp/0898716594/ref=sr_1_1?dchild=1&keywords=griewank&qid=1598888684&s=books&sr=1-1" target="_blank">Griewank and Walter (2008)</a></br>
        <a href="https://www.cs.jhu.edu/~jason/papers/eisner.spnlp16.pdf" target="_blank">Eisner (2016)</a></br>
        <a href="https://drive.google.com/file/d/1W4N_ZKOcs-g7gbQqSLRy6fc-Oc7fmKi7/view?usp=sharing" target="_blank">Backpropagation Proof</a></br>
        <a href="https://drive.google.com/file/d/1XWRz4yMi2A5BZSRSgnnbRJikqz7RYtrN/view?usp=sharing" target="_blank">Computation Graph for MLP</a></br>
        <a href="https://drive.google.com/file/d/1hsYIXXd6cEWocrhI-pQ4Ox8FG49Otu_m/view?usp=sharing" target="_blank">Computation Graph Example</a></td>
        <td><a href="https://drive.google.com/file/d/1Z_2Sjasl0IVjowxs1tkV81SYjP7iPXpb/view?usp=sharing" target="_blank">Week 2</a></br>
          <a href="https://drive.google.com/file/d/1IKObOq3QApeRDsEqKdkKI7CwjJ0ggkJF/view?usp=sharing" target="_blank">Solutions</a></td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>10.03.21</td>
      <td>Log-Linear Modeling---Meet the Softmax</td>
      <td><a href="https://drive.google.com/file/d/14gnMqCplpjoVVT0Q5Pt3YI5rOQqL6FMl/view?usp=sharing" target="_blank">Lecture 3</a></td>
      <td>Eisenstein Ch. 2</td>
      <td><a href="https://www.cs.jhu.edu/~jason/papers/ferraro+eisner.tnlp13.pdf" target="_blank">Ferraro and Eisner (2013)</a></br>
        <a href="http://cs.jhu.edu/~jason/tutorials/loglin/further.html">Jason Eisner’s list of further resources on log-linear modeling</a></td>
        <td><a href="https://drive.google.com/file/d/1c0ukuClgztpR3rMA8cFQs2-tj4ClBlmr/view?usp=sharing" target="_blank">Week 3</a></br>
          <a href="https://drive.google.com/file/d/1Dai8uwluiJZJt-ZHreG5XkX0IQIHQ60A/view?usp=sharing" target="_blank">Solutions</a></td>
    </tr>
    <tr>
      <th scope="row">4</th>
      <td>17.03.21</td>
      <td>Sentiment Analysis with Multi-layer Perceptrons</td>
      <td><a href="https://drive.google.com/file/d/1Dinfnb1tnK4zoN4bquh9F5D18bCNkGRs/view?usp=sharing" target="_blank">Lecture 4</a></td>
      <td>Eisenstein Ch. 3 and Ch. 4</br>Goodfellow, Bengio and Courville Ch. 6</td>
      <td><a href="https://en.wikipedia.org/wiki/Universal_approximation_theorem" target="_blank">Wikipedia</a></br>
        <a href="http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.441.7873&rep=rep1&type=pdf" target="_blank">Cybenko (1989)</a></br>
        <a href="https://arxiv.org/pdf/1710.11278.pdf" target="_blank">Hanin and Selke (2018)</a></br>
        <a href="https://www.cs.cornell.edu/home/llee/omsa/omsa.pdf" target="_blank">Pang and Lee (2008)</a></br>
        <a href="https://www.aclweb.org/anthology/P15-1162/" target="_blank">Iyyer et al. (2015)</a></br>
      <a href="https://arxiv.org/pdf/1411.2738.pdf" target="_blank">word2vec Parameter Learning Explained</a></br>
    <a href="https://arxiv.org/pdf/1402.3722.pdf" target="_blank">word2vec Explained</a></br></td>
    <td><a href="https://drive.google.com/file/d/1iPur9_Rx6GUW9oL9-RDMXsYP4g8HXFos/view?usp=sharing" target="_blank">Week 4</a></br>
          <a href="https://drive.google.com/file/d/1f83kDZRsVYUVb34VaGT-_H09t7HQCNE9/view?usp=sharing" target="_blank">Solutions</a></td>
    </tr>
    <tr>
      <th scope="row">5</th>
      <td>24.03.21</td>
      <td>Language Modeling with *n*-grams and LSTMs</td>
      <td><a href="https://drive.google.com/file/d/1TmY6psV5pjhKd_6Ur8n35f_TTcRUtyh_/view?usp=sharing" target="_blank">Lecture 5</a></td>
      <td>Eisenstein Ch. 6</br>Goodfellow, Bengio and Courville Ch. 10</td>
      <td><a href="https://nlp.stanford.edu/~wcmac/papers/20050421-smoothing-tutorial.pdf" target="_blank">Good Tutorial on n-gram smoothing</a></br>
        <a href="https://en.wikipedia.org/wiki/Good%E2%80%93Turing_frequency_estimation" target="_blank">Good–Turing Smoothing</a></br>
        <a href="https://ieeexplore.ieee.org/document/479394" target="_blank">Kneser and Ney (1995)</a></br>
        <a href="https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf" target="_blank">Bengio et al. (2003)</a></br>
        <a href="https://www.isca-speech.org/archive/archive_papers/interspeech_2010/i10_1045.pdf" target="_blank">Mikolov et al. (2010)</a></td>
        <td><a href="https://drive.google.com/file/d/11oINZRB5hbjW2SG3H0KalPE-4nlceNPY/view?usp=sharing" target="_blank">Week 5</a></br>
          <a href="https://drive.google.com/file/d/10KrxoxmFXpqd40OLiH3owK1hBJ2OWTap/view?usp=sharing" target="_blank">Solutions</a></td>
    </tr>
    <tr>
      <th scope="row">6</th>
      <td>31.03.21</td>
      <td>Part-of-Speech Tagging with CRFs</td>
      <td><a href="https://drive.google.com/file/d/16jvZdoMmr4SAUKJaN3PeDi-nlWF82_xF/view?usp=sharing" target="_blank">Lecture 6</a></td>
      <td>Eisenstein Ch. 7 and 8</td>
      <td><a href="https://timvieira.github.io/blog/post/2015/04/29/multiclass-logistic-regression-and-conditional-random-fields-are-the-same-thing/" target="_blank">Tim Vieira's Blog</a></br>
        <a href="https://dl.acm.org/doi/10.5555/645529.658277" target="_blank">McCallum et al. (2000)</a></br>
        <a href="https://repository.upenn.edu/cgi/viewcontent.cgi?article=1162&context=cis_papers" target="_blank">Lafferty et al. (2001)</a></br>
        <a href="https://homepages.inf.ed.ac.uk/csutton/publications/crftut-fnt.pdf" target="_blank">Sutton and McCallum (2011)</a></br>
        <a href="https://mitpress.mit.edu/books/probabilistic-graphical-models" target="_blank">Koller and Friedman (2009)</a></td>
        <td><a href="https://drive.google.com/file/d/1CbQBGsh9xTkDVze0oTORrN3S3VIr3DFg/view?usp=sharing" target="_blank">Week 6</a></br>
          <a href="https://drive.google.com/file/d/1-q7bz1kx89j2a8_8Yq--qXSVDzsy4YJb/view?usp=sharing" target="_blank">Solutions</a></td>
    </tr>
    <tr>
      <th scope="row">7</th>
      <td>14.4.21</td>
      <td>Context-Free Parsing with CKY</td>
      <td><a href="https://drive.google.com/file/d/1RIbjaBSnypeu3gRJGmsGGVUF8J3o2tbZ/view?usp=sharing" target="_blank">Lecture 7</a></td>
      <td>Eisenstein Ch. 10</td>
      <td><a href="http://www.cs.columbia.edu/~mcollins/io.pdf" target="_blank">The Inside-Outside Algorithm</a></br>
        <a href="https://www.cs.jhu.edu/~jason/465/PowerPoint/lect08-parse.ppt" target="_blank">Jason Eisner’s Slides</a></br>
        <a href="https://www.ideals.illinois.edu/handle/2142/74304">Kasami (1966)</a></br>
        <a href="https://www.sciencedirect.com/science/article/pii/S001999586780007X?via%3Dihub" target="_blank">Younger (1967)</a></br>
        <a href="http://www.softwarepreservation.org/projects/FORTRAN/CockeSchwartz_ProgLangCompilers.pdf" target="_blank">Cocke and Schwartz (1970)</a></td>
        <td><a href="https://drive.google.com/file/d/1nKp10BoJY5AdsXa3AmufSUTG-HMIeSoX/view?usp=sharing" target="_blank">Week 7</a></br>
          <a href="https://drive.google.com/file/d/1wrRnTAIBtSy8SO6Ye3VamqizTcq130A-/view?usp=sharing" target="_blank">Solutions</a></br>
          <a href="https://drive.google.com/file/d/1zJXpRrYIZpbQEgPv765NGHVw3G4mvHLA/view?usp=sharing" target="_blank">Coding Exercise</a></br>
          <a href="https://drive.google.com/file/d/16q07tVT-HvOA4260dYoSR-VKvIBS9hD8/view?usp=sharing" target="_blank">Coding Solutions</a>
    </tr>
    <tr>
      <th scope="row">-</th>
      <td>21.4.21</td>
      <td>Lecture cancelled</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th scope="row">8</th>
      <td>28.4.21</td>
      <td>Dependency Parsing with the Matrix-Tree Theorem</td>
      <td><a href="https://drive.google.com/file/d/1rztIaNxua6J5NkSGTLolqyUT9UDKcsQX/view?usp=sharing" target="_blank">Lecture 8</a></td>
      <td>Eisenstein Ch. 11</td>
      <td><a href="https://www.aclweb.org/anthology/D07-1015/" target="_blank">Koo et al. (2007)</a></br>
        <a href="https://www.aclweb.org/anthology/D07-1014/" target="_blank">Smith and Smith (2007)</a></br>
        <a href="https://www.aclweb.org/anthology/W07-2216/" target="_blank">McDonald and Satta (2007)</a></br>
        <a href="https://www.morganclaypool.com/doi/abs/10.2200/S00169ED1V01Y200901HLT002" target="_blank">McDonald, Kübler and Nivre (2009)</a></td>
        <td><a href="https://drive.google.com/file/d/1-AKW_NzSMXXUVgBD1FBN2xOOTUGkpxq5/view?usp=sharing" target="_blank">Week 8</a></br>
          <a href="https://drive.google.com/file/d/1jd3FNdPrDkLQ7TB75svham8WDPqNmpxo/view?usp=sharing" target="_blank">Solutions</a></td>
    </tr>
    <tr>
      <th scope="row">9</th>
      <td>5.5.21</td>
      <td>Semantic Parsing with CCGs</td>
      <td><a href="https://drive.google.com/file/d/1e7RVwqWpvP7wBmYEtWFM0DWe7brwoETu/view?usp=sharing" target="_blank">Lecture 9</a></td>
      <td>Eisenstein Ch. 9.3 and 12</td>
      <td><a href="https://www.aclweb.org/anthology/P88-1034/" target="_blank">Weir and Joshi (1988)</a></br>
        <a href="https://www.aclweb.org/anthology/Q14-1032/" target="_blank">Kuhlmann and Satta (2014)</a></br>
        <a href="https://homepages.inf.ed.ac.uk/steedman/papers/ccg/ikdoz17.2.pdf" target="_blank">Mark Steedman's CCG slides</a></td>
      <td><a href="https://drive.google.com/file/d/1oRojvYSeG80Ght-YtYDoY5TIgZOPhBhv/view?usp=sharing" target="_blank">Week 9</a></br>
        <a href="https://drive.google.com/file/d/1mK98TyTLHJD-SJJBkUMUH2_2dLcF1QkA/view?usp=sharing" target="_blank">Solutions</a></td>
    </tr>
    <tr>
      <th scope="row">10</th>
      <td>12.5.21</td>
      <td>Transliteration with WFSTs</td>
      <td><a href="https://drive.google.com/file/d/1SBZGZnkRbWrQaBYicocCpG15EcFSHxme/view?usp=sharing" target="_blank">Lecture 10</a></td>
      <td>Eisenstein Ch. 9</td>
      <td><a href="https://www.aclweb.org/anthology/J98-4003.pdf" target="_blank">Knight and Graehl (1998)</a></br>
        <a href="https://cs.nyu.edu/~mohri/pub/hbka.pdf" target="_blank">Mohri, Pereira and Riley (2008)</a></td>
      <td><a href="https://drive.google.com/file/d/1s4X8ojXAFLtIaFlcLEI6dHur13p8CG6A/view?usp=sharing" target="_blank">Week 10</a></br>
        <a href="https://drive.google.com/file/d/1zsJwrGte2375agRpa7TgV-Me-FaWhSvX/view?usp=sharing" target="_blank">Solutions</a></td>
    </tr>
    <tr>
      <th scope="row">11</th>
      <td>19.5.21</td>
      <td>Machine Translation with Transformers</td>
      <td><a href="https://drive.google.com/file/d/1008UHRtJPtJIsTBtC1yOa6RrSJaidhke/view?usp=sharing" target="_blank">Lecture 11</a></td>
      <td>Eisenstein Ch. 18</td>
      <td><a href="https://www.amazon.com/gp/product/1108497322/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1108497322&linkCode=as2&tag=statismachint-20&linkId=ca7b8315b48f309c992019761c3ac4e4" target="_blank">Neural Machine Translation</a></br>
        <a href="https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf" target="_blank">Vaswani et al. (2017)</a></br>
        <a href="https://www.aclweb.org/anthology/W18-2509/">Rush (2018)</a></td>
      <td><a href="https://drive.google.com/file/d/1EKXzkmbjXyxvn0i3PMzRKh96vZQ7iv7x/view?usp=sharing" target="_blank">Week 11</a></br>
        <a href="https://drive.google.com/file/d/1le3KDU1J5juI7d1v_4hqXr_n2TocrMIY/view?usp=sharing" target="_blank">Solutions</a></td>
    </tr>
    <tr>
      <th scope="row">12</th>
      <td>26.5.21</td>
      <td>Axes of Modeling</td>
      <td><a href="https://drive.google.com/file/d/1JhLdKPxcalIk65F9Frdkgj2nr8RNCjLH/view?usp=sharing" target="_blank">Lecture 12</a></td>
      <td>Review: Eisenstein Ch. 2</br>Goodfellow, Bengio and Courville Ch. 5 and 11</td>
      <td></td>
      <td><a href="https://drive.google.com/file/d/1vCttVzDm4rM_s4oJ85byk2BvIgFfjEgJ/view?usp=sharing" target="_blank">Week 12</a></br>
        <a href="https://drive.google.com/file/d/1ra2iP0f9HFCd2s9m0vouVuz39J-i42bZ/view?usp=sharing" target="_blank">Solutions</a></td>
    </tr>
    <tr>
      <th scope="row">13</th>
      <td>2.6.21</td>
      <td>Bias and Fairness in NLP</td>
      <td><a href="https://drive.google.com/file/d/1AOUrM7LyXfRg-ygPsy2_4jjwuj2lyiR4/view?usp=sharing" target="_blank">Lecture 13</a></td>
      <td></td>
      <td><a href="https://papers.nips.cc/paper/6228-man-is-to-computer-programmer-as-woman-is-to-homemaker-debiasing-word-embeddings.pdf" target="_blank">Bolukabasi et al. (2016)</a></br>
        <a href="https://arxiv.org/abs/1903.03862" target="_blank">Gonen and Goldberg (2019)</a></br>
        <a href="https://arxiv.org/abs/1909.00871" target="_blank">Hall Maudslay et al. (2019)</a></br>
        <a href="https://arxiv.org/abs/2009.09435" target="_blank">Vargas and Cotterell (2020)</a></br>
        <a href="http://ciml.info/dl/v0_99/ciml-v0_99-ch08.pdf" target="_blank">A Course in Machine Learning Chapter 8</a></td>
      <td></td>
    </tr>
    
  </tbody>
</table>

## Weekly Exercises

We will release exercises every week that cover material in the next lecture (e.g., exercises released on Sunday night cover material in the following Wednesday's lecture). These exercises are intended to give you the opportunity to test your understanding of the course material. They are not for a grade, nor will the TAs be able to offer individual feedback on your solutions. If you have questions regarding the exercises, we recommend bringing them to the **discussion section** that week as the TAs will walk through related problems. Solutions will be released in the following week.

## Course Project/Assignment

Every student has the option of completing *either* a research project or a structured assignment. This work will be worth 30% of your final mark. Both will be due on **July 15th.**

The **research project** is an open-ended project where students reimplement an existing research paper or perform novel research if they are so inclined. Projects can be completed in groups of up to 4; feel free to use Piazza to reach out to other students in the course. We will require you to write a 1-page project proposal where we will give you feedback on the idea (due **March 31st**). Submission can be done on the course Moodle page (one submission per team please). We will also require a progress report (due **May 31st**). Please send both the progress and final reports (including your recorded presentation) directly to your assigned TA. More details can be found in the [project guidelines](https://drive.google.com/file/d/125XGqBMwGHpFc6pS1JNhmbEXFpt_hGHC/view?usp=sharing).

In the **assignment**, some of the questions will be more theoretical and resemble the questions you will see on the final exam. However, there will also be a substantial coding portion, which would not look like the exam questions. For instance, we may ask you to implement a recurrent neural dependency parser. Assignments must be completed individually, although you may discuss the assignment with other students. If you choose to do so, you must specify with whom you collaborated in your submission (see template below). We will release the assignment in two waves, corresponding to when course material is covered. The second portion of the assignment will be released ~**May 20th**. **Submission:** Upload a zip file (with a single pdf containing all written answers to both parts of the assignment and the colab notebooks) to the assignment submission task on Moodle. For the writeup portion, we will only process a single pdf: if you include multiple pdfs in your submission, only one will be graded.  

## Materials

- [Project Guidelines](https://drive.google.com/file/d/125XGqBMwGHpFc6pS1JNhmbEXFpt_hGHC/view?usp=sharing) 
- [Assignment Part 1](https://drive.google.com/file/d/1fnkBBeNn26ILyWj34a2gpZTUBGRMA8wu/view?usp=sharing)  
- [Assignment Part 2](https://drive.google.com/file/d/1QNKLRE6elssUuypZbOwFO51CMvoeRgbT/view?usp=sharing)  
- [Assignment Submission Template](https://www.overleaf.com/read/vdpvbjpwrrvb)
- [Exam Topics](https://docs.google.com/document/d/1EsJpCvdeS1KboidK87LS658wYyaUed3cZIqstWIa-fY/edit?usp=sharing)
- [Practice Exam](https://drive.google.com/file/d/1Fs0CYuLG-sBLZJwthChU8wqYyzBBOoPi/view?usp=sharing)
- [Practice Exam Solutions](https://drive.google.com/file/d/1sv4GoNrAtRzlV5Ddk9JqBxe2IgTX_ttv/view?usp=sharing)

<!-- ### Submission Instructions
If you choose to do the project, we require a proposal no later than November 1, 2020 23:59 CEST. Further, a progress report is due December 11, 2020 23:59 CEST. Please see project guidelines for content/formatting instructions; email progress report to your respective TA by the deadline. 

The writeup for all projects/assigments will be due on **January 15, 2021**. Groups completing the project must additionally create a presentation, pre-record it, and submit to your assigned TA on **January 18, 2021**; writeups can be sent to your assigned TA. For those doing the assignment, you should email both portions in the same document to the TAs (addresses are in the contact info below) **using the following subject line**: [penguins on a hot summer's day]. Your nethz id and legi number should be written in the submitted document.


- [Course Assignment: Part 1](https://drive.google.com/file/d/1EcLANxfCsW8xHyT8JYB7CSVYp8WxNQhP/view?usp=sharing)
- [Course Assignment: Part 2](https://drive.google.com/file/d/1reiP73K6Et07ZSTM_7VDpUM26wZ3it3q/view?usp=sharing)
- [Course Assignment LaTex Template](https://www.overleaf.com/read/vdpvbjpwrrvb)
- [Draft of assignment solutions](https://drive.google.com/file/d/1M-7gcorQRmT4uWFr5wMzrE6tKpz6VS4y/view?usp=sharing) -->

## Contact
You can ask questions on [piazza](https://www.piazza.com/ethz.ch/spring2021/252300500l). Please post questions there, so others can see them and share in the discussion. If you have questions which are not of general interest, please don't hesitate to contact us directly, i.e., post a private note on piazza or email Ryan with Clara cc-ed.

<!-- <table class="table">
  <tbody>
    <tr>
      <td>Lecturer</td>
      <td><a href="mailto:ryan.cotterell@inf.ethz.ch">Ryan Cotterell</a></td>
    </tr>
    <tr>
      <td>Teaching Assistants</td>
      <td><a href="mailto:meistecl@inf.ethz.ch">Clara Meister</a>, <a href="mailto:niklas.stoehr@inf.ethz.ch">Niklas Stoehr</a>, <a href="mailto:selena.pepic@inf.ethz.ch">Selena Pepic</a>, <a href="mailto:mkuznetsova@inf.ethz.ch">Rita Kuznetsova</a>, <a href="mailto:asvete@student.ethz.ch">Anej Svete</a>, <a href="mailto:abutoi@student.ethz.ch">Alexandra Butoi</a>, <a href="mailto:anrael@ethz.ch">Anton Rael</a>, <a href="mailto:dwissel@student.ethz.ch">David Wissel</a>, <a href="mailto:rajai.nasser@inf.ethz.ch">Rajai Nasser</a>, <a href="mailto:aamini@student.ethz.ch">Afra Amini</a>, <a href="mailto:alberto.pennino@inf.ethz.ch">Alberto Pennino</a>, <a href="mailto:alexander.immer@inf.ethz.ch
">Alexander Immer</a></td>
    </tr>

    
  </tbody>
</table> -->
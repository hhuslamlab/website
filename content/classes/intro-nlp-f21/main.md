
+++
title = 'Natural Language Processing'
subtitle = 'ETH Zürich, Fall 2021: [Course catalog](http://www.vvz.ethz.ch/Vorlesungsverzeichnis/lerneinheit.view?semkez=2021W&ansicht=ALLE&lerneinheitId=148639&lang=en)'
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
* **30%** Course Project *or* Assignment


**Lectures:** Mon 12-14h Zoom (recurring link sent at start of semester). Recordings can be found in the password-protected course Polybox: https://polybox.ethz.ch/index.php/s/gplfKPSDUHSXDRq. The password can be found on the Moodle home page for the course.    

**Discussion Sections:** Weds 12-14h HG F7; discussion sections will either be in person or via Zoom (same link as lecture), depending on the individual preferences of the teaching staff. Regardless, all sections will be recorded. Schedule to be posted at the beginning of the semester.

**Textbooks:** [Introduction to Natural Language Processing (Eisenstein)](https://www.amazon.de/Jacob-Eisenstein/dp/0262042843/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=30OMHV1C018JY&dchild=1&keywords=introduction+to+natural+language+processing&qid=1598878964&sprefix=introduction+to+na%2Caps%2C148&sr=8-1)  
&emsp;&emsp;&emsp;&emsp;&emsp; [Deep Learning (Goodfellow, Bengio and Courville)](https://www.deeplearningbook.org/)  


## News

**18.09** &emsp; Class website is online!  
**18.09** &emsp; We are using Moodle as our discussion forum.  
**27.09** &emsp; First lecture.  
**13.10** &emsp; First discussion section.  
**03.10** &emsp; [Project guidelines](https://drive.google.com/file/d/125XGqBMwGHpFc6pS1JNhmbEXFpt_hGHC/view?usp=sharing) released.    
**31.10** &emsp; Project proposals due.  
**01.04** &emsp; [Assignment Part 1](https://drive.google.com/file/d/1fnkBBeNn26ILyWj34a2gpZTUBGRMA8wu/view?usp=sharing) released.  
**03.12** &emsp; [Assignment Part 2](https://drive.google.com/file/d/19ZEn0NJmxxVJOiPV2cdfyJ-9YznCwK-r/view?usp=sharing) released. 

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
      <th scope="col" style='white-space:nowrap'>Discussion Section</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>27.09.21</td>
      <td>Introduction to Natural Language</td>
      <td><a href="https://drive.google.com/file/d/10KPQWpaDhfUBosCyc-ngbWvOCmiCJPpg/view?usp=sharing" target="_blank">Lecture 1</a></td>
      <td>Eisenstein Ch. 1</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>4.10.21</td>
      <td>Backpropagation</td>
      <td><a href="https://drive.google.com/file/d/125ASMverltb8UUV7w9oVGhbCPhk49Zq_/view?usp=sharing" target="_blank">Lecture 2</a></td>
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
        <td><a href="https://drive.google.com/file/d/1Z_2Sjasl0IVjowxs1tkV81SYjP7iPXpb/view?usp=sharing" target="_blank">Exercises</a></br><a href="https://drive.google.com/file/d/1IKObOq3QApeRDsEqKdkKI7CwjJ0ggkJF/view?usp=sharing" target="_blank">(<em>Solutions</em>)</a></td>
        <td>13.10.21 (online)</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>11.10.21</td>
      <td>Log-Linear Modeling---Meet the Softmax</td>
      <td><a href="https://drive.google.com/file/d/1-zDjQ36vWuNpYMd-S_xIi3YSncLaVImp/view?usp=sharing" target="_blank">Lecture 3</a></td>
      <td>Eisenstein Ch. 2</td>
      <td><a href="https://www.cs.jhu.edu/~jason/papers/ferraro+eisner.tnlp13.pdf" target="_blank">Ferraro and Eisner (2013)</a></br>
        <a href="http://cs.jhu.edu/~jason/tutorials/loglin/further.html">Jason Eisner’s list of further resources on log-linear modeling</a></td>
        <td><a href="https://drive.google.com/file/d/1c0ukuClgztpR3rMA8cFQs2-tj4ClBlmr/view?usp=sharing" target="_blank">Exercises</a></br><a href="https://drive.google.com/file/d/1J0_ZcQbCkGI7Xhbfl2iWax5i0gd-2725/view?usp=sharing" target="_blank">(<em>Solutions</em>)</a></td>
        <td>20.10.21 (in person)</br><a href="https://drive.google.com/file/d/1SkyIuFbxmjHJ2mDod0j77mYTRd5GyVWA/view?usp=sharing" target="_blank">Notes</a></td>
    </tr>
    <tr>
      <th scope="row">4</th>
      <td>18.10.21</td>
      <td>Sentiment Analysis with Multi-layer Perceptrons</td>
      <td><a href="https://drive.google.com/file/d/1YcmNtg6UcqESmX43Fe9okNOiTScf8Vyj/view?usp=sharing" target="_blank">Lecture 4</a></td>
      <td>Eisenstein Ch. 3 and Ch. 4</br>Goodfellow, Bengio and Courville Ch. 6</td>
      <td><a href="https://en.wikipedia.org/wiki/Universal_approximation_theorem" target="_blank">Wikipedia</a></br>
        <a href="http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.441.7873&rep=rep1&type=pdf" target="_blank">Cybenko (1989)</a></br>
        <a href="https://arxiv.org/pdf/1710.11278.pdf" target="_blank">Hanin and Selke (2018)</a></br>
        <a href="https://www.cs.cornell.edu/home/llee/omsa/omsa.pdf" target="_blank">Pang and Lee (2008)</a></br>
        <a href="https://www.aclweb.org/anthology/P15-1162/" target="_blank">Iyyer et al. (2015)</a></br>
      <a href="https://arxiv.org/pdf/1411.2738.pdf" target="_blank">word2vec Parameter Learning Explained</a></br>
    <a href="https://arxiv.org/pdf/1402.3722.pdf" target="_blank">word2vec Explained</a></br></td>
    <td><a href="https://drive.google.com/file/d/1-gAvUCK2Sqee4THo_4LwUCICfwtZgX-r/view?usp=sharing" target="_blank">Exercises</a></br><a href="https://drive.google.com/file/d/1pHL9KlaJehuKwKRtr6FWsxAmegS3hnIx/view?usp=sharing" target="_blank">(<em>Solutions</em>)</a></br><a href="https://colab.research.google.com/drive/1gngt93hfpf4CAhJr5Kk9xH4evtLfwdcb?usp=sharing" target="_blank">Coding Exercises</a></br><a href="https://colab.research.google.com/drive/1WUy4G2SsoLelrZDkO2I0v9tHx9x27NJK?usp=sharing" target="_blank">(<em>Coding Solutions</em>)</a></td>
    <td>27.10.21 (online)</td>
    </tr>
    <tr>
      <th scope="row">5</th>
      <td>25.10.21</td>
      <td>Language Modeling with <em>n</em>-grams and LSTMs</td>
      <td><a href="https://drive.google.com/file/d/1XX72vGgUX2-50tKu4K13AdGOSV6cDEv0/view?usp=sharing">Lecture 5</a></td>
      <td>Eisenstein Ch. 6</br>Goodfellow, Bengio and Courville Ch. 10</td>
      <td><a href="https://nlp.stanford.edu/~wcmac/papers/20050421-smoothing-tutorial.pdf" target="_blank">Good Tutorial on n-gram smoothing</a></br>
        <a href="https://en.wikipedia.org/wiki/Good%E2%80%93Turing_frequency_estimation" target="_blank">Good–Turing Smoothing</a></br>
        <a href="https://ieeexplore.ieee.org/document/479394" target="_blank">Kneser and Ney (1995)</a></br>
        <a href="https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf" target="_blank">Bengio et al. (2003)</a></br>
        <a href="https://www.isca-speech.org/archive/archive_papers/interspeech_2010/i10_1045.pdf" target="_blank">Mikolov et al. (2010)</a></td>
        <td><a href="https://drive.google.com/file/d/11oINZRB5hbjW2SG3H0KalPE-4nlceNPY/view?usp=sharing" target="_blank">Exercises</a></br><a href="https://drive.google.com/file/d/10KrxoxmFXpqd40OLiH3owK1hBJ2OWTap/view?usp=sharing" target="_blank">(<em>Solutions</em>)</a></td>
        <td>3.11.21 (online)</td>
    </tr>
    <tr>
      <th scope="row">6</th>
      <td>01.11.21</td>
      <td>Part-of-Speech Tagging with CRFs</td>
      <td><a href="https://drive.google.com/file/d/1RleLx-bnQzByyVVKH5enaipNBEqnADcM/view?usp=sharing" target="_blank">Lecture 6</a></td>
      <td>Eisenstein Ch. 7 and 8</td>
      <td><a href="https://timvieira.github.io/blog/post/2015/04/29/multiclass-logistic-regression-and-conditional-random-fields-are-the-same-thing/" target="_blank">Tim Vieira's Blog</a></br>
        <a href="https://dl.acm.org/doi/10.5555/645529.658277" target="_blank">McCallum et al. (2000)</a></br>
        <a href="https://repository.upenn.edu/cgi/viewcontent.cgi?article=1162&context=cis_papers" target="_blank">Lafferty et al. (2001)</a></br>
        <a href="https://homepages.inf.ed.ac.uk/csutton/publications/crftut-fnt.pdf" target="_blank">Sutton and McCallum (2011)</a></br>
        <a href="https://mitpress.mit.edu/books/probabilistic-graphical-models" target="_blank">Koller and Friedman (2009)</a></td>
        <td><a href="https://drive.google.com/file/d/1IXVYz_PvbjOpyKX_1dGnTZtEd2KTGqqU/view?usp=sharing">Exercises</a></br><a href="https://drive.google.com/file/d/1-q7bz1kx89j2a8_8Yq--qXSVDzsy4YJb/view?usp=sharing" target="_blank">(<em>Solutions</em>)</a></td>
        <td>10.11.21 (online)</td>
    </tr>
    <tr>
      <th scope="row">7</th>
      <td>08.11.21</td>
      <td>Context-Free Parsing with CKY</td>
      <td><a href="https://drive.google.com/file/d/1w-yfftBJPzNDAK8zdaX9aRa2n6ZdmYvP/view?usp=sharing">Lecture 7</a></td>
      <td>Eisenstein Ch. 10</td>
      <td><a href="http://www.cs.columbia.edu/~mcollins/io.pdf" target="_blank">The Inside-Outside Algorithm</a></br>
        <a href="https://www.cs.jhu.edu/~jason/465/PowerPoint/lect08-parse.ppt" target="_blank">Jason Eisner’s Slides</a></br>
        <a href="https://www.ideals.illinois.edu/handle/2142/74304">Kasami (1966)</a></br>
        <a href="https://www.sciencedirect.com/science/article/pii/S001999586780007X?via%3Dihub" target="_blank">Younger (1967)</a></br>
        <a href="http://www.softwarepreservation.org/projects/FORTRAN/CockeSchwartz_ProgLangCompilers.pdf" target="_blank">Cocke and Schwartz (1970)</a></td>
        <td><a href="https://drive.google.com/file/d/1nKp10BoJY5AdsXa3AmufSUTG-HMIeSoX/view?usp=sharing">Exercises</a></br><a href="https://drive.google.com/file/d/1dHfSe9_JchHs-4LD4gUgDVrCwf1G4t4L/view?usp=sharing" target="_blank">(<em>Solutions</em>)</a></br><a href="https://drive.google.com/file/d/1zJXpRrYIZpbQEgPv765NGHVw3G4mvHLA/view?usp=sharing">Coding Exercises</a></br><a href="https://drive.google.com/file/d/16q07tVT-HvOA4260dYoSR-VKvIBS9hD8/view?usp=sharing" target="_blank">(<em>Coding Solutions</em>)</a></td>
        <td>17.11.21 (online)</td>
    </tr>
    <tr>
      <th scope="row">8</th>
      <td>15.11.21</td>
      <td>Dependency Parsing with the Matrix-Tree Theorem</td>
      <td><a href="https://drive.google.com/file/d/1GdCIUqjju_2hqCPK_WfqBLpl9yx2COfe/view?usp=sharing" target="_blank">Lecture 8</a></td>
      <td>Eisenstein Ch. 11</td>
      <td><a href="https://www.aclweb.org/anthology/D07-1015/" target="_blank">Koo et al. (2007)</a></br>
        <a href="https://www.aclweb.org/anthology/D07-1014/" target="_blank">Smith and Smith (2007)</a></br>
        <a href="https://www.aclweb.org/anthology/W07-2216/" target="_blank">McDonald and Satta (2007)</a></br>
        <a href="https://www.morganclaypool.com/doi/abs/10.2200/S00169ED1V01Y200901HLT002" target="_blank">McDonald, Kübler and Nivre (2009)</a></td>
        <td><a href="https://drive.google.com/file/d/1-AKW_NzSMXXUVgBD1FBN2xOOTUGkpxq5/view?usp=sharing">Exercises</a></br><a href="https://drive.google.com/file/d/1jd3FNdPrDkLQ7TB75svham8WDPqNmpxo/view?usp=sharing" target="_blank">(<em>Solutions</em>)</a></td>
        <td>24.11.21 (in person)</td>
    </tr>
    <tr>
      <th scope="row">9</th>
      <td>22.11.21</td>
      <td>Semantic Parsing with CCGs</td>
      <td><a href="https://drive.google.com/file/d/1e7RVwqWpvP7wBmYEtWFM0DWe7brwoETu/view?usp=sharing" target="_blank">Lecture 9</a></td>
      <td>Eisenstein Ch. 9.3 and 12</td>
      <td><a href="https://www.aclweb.org/anthology/P88-1034/" target="_blank">Weir and Joshi (1988)</a></br>
        <a href="https://www.aclweb.org/anthology/Q14-1032/" target="_blank">Kuhlmann and Satta (2014)</a></br>
        <a href="https://homepages.inf.ed.ac.uk/steedman/papers/ccg/ikdoz17.2.pdf" target="_blank">Mark Steedman's CCG slides</a></td>
      <td><a href="https://drive.google.com/file/d/1oRojvYSeG80Ght-YtYDoY5TIgZOPhBhv/view?usp=sharing">Exercises</a></br><a href="https://drive.google.com/file/d/1mK98TyTLHJD-SJJBkUMUH2_2dLcF1QkA/view?usp=sharing" target="_blank">(<em>Solutions</em>)</a></td>
      <td>1.12.21 (in person)</br><a href="https://drive.google.com/file/d/1SQyjRs5CxYcexsPAQ2JqiSq03oEKAAwt/view?usp=sharing" target="_blank">Notes</a></td>
    </tr>
    <tr>
      <th scope="row">10</th>
      <td>29.11.21</td>
      <td>Transliteration with WFSTs</td>
      <td><a href="https://drive.google.com/file/d/1SBZGZnkRbWrQaBYicocCpG15EcFSHxme/view?usp=sharing" target="_blank">Lecture 10</a></td>
      <td>Eisenstein Ch. 9</td>
      <td><a href="https://www.aclweb.org/anthology/J98-4003.pdf" target="_blank">Knight and Graehl (1998)</a></br>
        <a href="https://cs.nyu.edu/~mohri/pub/hbka.pdf" target="_blank">Mohri, Pereira and Riley (2008)</a></td>
      <td><a href="https://drive.google.com/file/d/1s4X8ojXAFLtIaFlcLEI6dHur13p8CG6A/view?usp=sharing">Exercises</a></br><a href="https://drive.google.com/file/d/1zsJwrGte2375agRpa7TgV-Me-FaWhSvX/view?usp=sharing" target="_blank">(<em>Solutions</em>)</a></td>
      <td>8.12.21 (online)</td>
    </tr>
    <tr>
      <th scope="row">11</th>
      <td>5.12.21</td>
      <td>Machine Translation with Transformers</td>
      <td><a href="https://drive.google.com/file/d/1clflxhvjOn2liT5aRSbCAXyp73J6c2X3/view?usp=sharing" target="_blank">Lecture 11</a></td>
      <td>Eisenstein Ch. 18</td>
      <td><a href="https://www.amazon.com/gp/product/1108497322/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1108497322&linkCode=as2&tag=statismachint-20&linkId=ca7b8315b48f309c992019761c3ac4e4" target="_blank">Neural Machine Translation</a></br>
        <a href="https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf" target="_blank">Vaswani et al. (2017)</a></br>
        <a href="https://www.aclweb.org/anthology/W18-2509/">Rush (2018)</a></td>
      <td><a href="https://drive.google.com/file/d/1EKXzkmbjXyxvn0i3PMzRKh96vZQ7iv7x/view?usp=sharing">Exercises</a></br><a href="https://drive.google.com/file/d/1Lk6W6zaOSkVd4-tDl0r75x3PU1frmoU1/view?usp=sharing" target="_blank">(<em>Solutions</em>)</a></td>
      <td>15.12.21 (online)</br><a href="https://drive.google.com/file/d/1UgxV3DE56F9_WCYD1aPNeXaZUgmcOm6n/view?usp=sharing" target="_blank">Notes</a></br><a href="https://drive.google.com/file/d/1MPEJTaObQVFo54ueCfsgM-XD3L8sdfEQ/view?usp=sharing" target="_blank">Code</a></td>
    </tr>
    <tr>
      <th scope="row">12</th>
      <td>13.12.21</td>
      <td>Axes of Modeling</td>
      <td><a href="https://drive.google.com/file/d/1rS8ntv8N0phphXeSCY6ly4X965twXxbE/view?usp=sharing">Lecture 12</a></td>
      <td>Review: Eisenstein Ch. 2</br>Goodfellow, Bengio and Courville Ch. 5 and 11</td>
      <td></td>
      <td><a href="https://drive.google.com/file/d/1vCttVzDm4rM_s4oJ85byk2BvIgFfjEgJ/view?usp=sharing">Exercises</a></br><a href="https://drive.google.com/file/d/1ra2iP0f9HFCd2s9m0vouVuz39J-i42bZ/view?usp=sharing">(<em>Solutions</em>)</a></td>
      <td>22.12.21 (in person)</br><a href="https://drive.google.com/file/d/16rku4FSctXERGXUf0DXTkgidK3yp7EDr/view?usp=sharing" target="_blank">Notes</a></td>
    </tr>
    <tr>
      <th scope="row">13</th>
      <td>20.12.21</td>
      <td>Bias and Fairness in NLP</td>
      <td><a href="https://drive.google.com/file/d/1AOUrM7LyXfRg-ygPsy2_4jjwuj2lyiR4/view?usp=sharing" target="_blank">Lecture 13</a></td>
      <td></td>
      <td><a href="https://papers.nips.cc/paper/6228-man-is-to-computer-programmer-as-woman-is-to-homemaker-debiasing-word-embeddings.pdf" target="_blank">Bolukabasi et al. (2016)</a></br>
        <a href="https://arxiv.org/abs/1903.03862" target="_blank">Gonen and Goldberg (2019)</a></br>
        <a href="https://arxiv.org/abs/1909.00871" target="_blank">Hall Maudslay et al. (2019)</a></br>
        <a href="https://arxiv.org/abs/2009.09435" target="_blank">Vargas and Cotterell (2020)</a></br>
        <a href="http://ciml.info/dl/v0_99/ciml-v0_99-ch08.pdf" target="_blank">A Course in Machine Learning Chapter 8</a></td>
      <td></td>
      <td></td>
    </tr>
    
  </tbody>
</table>

## Weekly Exercises

We will release exercises every week that cover lecture material. Exercises will be released the day of the relevant lecture and reviewed in the discussion section the following week (i.e., 9 days later). These exercises are intended to give you the opportunity to test your understanding of the course material. They are not for a grade, nor will the TAs be able to offer individual feedback on your solutions. If you have questions regarding the exercises, we recommend bringing them to the relevant **discussion section** as the TAs will walk through related problems. Solutions will be released in the following week.

## Course Project/Assignment

Every student has the option of completing *either* a research project or a structured assignment. This work will be worth 30% of your final mark. Both will be due on **January 15th, 2022.**

The **research project** is an open-ended project where students reimplement an existing research paper or perform novel research if they are so inclined. Projects can be completed in groups of up to 4. We will require you to write a 1-page project proposal where we will give you feedback on the idea (due **October 31st**). Submission can be done on the course Moodle page (one submission per team please). We will also require a progress report. Please send both the progress and final reports (including your recorded presentation) directly to your assigned TA. More details can be found in the [project guidelines](https://drive.google.com/file/d/125XGqBMwGHpFc6pS1JNhmbEXFpt_hGHC/view?usp=sharing). 

In the **assignment**, some of the questions will be more theoretical and resemble the questions you will see on the final exam. However, there will also be a substantial coding portion, which would not look like the exam questions. For instance, we may ask you to implement a recurrent neural dependency parser. Assignments must be completed individually, although you may discuss the assignment with other students. If you choose to do so, you must specify with whom you collaborated in your submission (see template below). We will release the assignment in two waves, corresponding to when course material is covered. **Submission:** Upload a zip file (with a single pdf containing all written answers to both parts of the assignment and the colab notebook) to the assignment submission task on Moodle. For the writeup portion, we will only process a single pdf: if you include multiple pdfs in your submission, only one will be graded.  

## Materials

- [Project Guidelines](https://drive.google.com/file/d/125XGqBMwGHpFc6pS1JNhmbEXFpt_hGHC/view?usp=sharing) 
- [Assignment Part 1](https://drive.google.com/file/d/1fnkBBeNn26ILyWj34a2gpZTUBGRMA8wu/view?usp=sharing)
- [Assignment Part 2](https://drive.google.com/file/d/19ZEn0NJmxxVJOiPV2cdfyJ-9YznCwK-r/view?usp=sharing)  
- [Assignment Submission Template](https://www.overleaf.com/read/vdpvbjpwrrvb)


<!-- - [Exam Topics](https://docs.google.com/document/d/1EsJpCvdeS1KboidK87LS658wYyaUed3cZIqstWIa-fY/edit?usp=sharing)
- [Practice Exam](https://drive.google.com/file/d/1Fs0CYuLG-sBLZJwthChU8wqYyzBBOoPi/view?usp=sharing)
- [Practice Exam Solutions](https://drive.google.com/file/d/1sv4GoNrAtRzlV5Ddk9JqBxe2IgTX_ttv/view?usp=sharing)
 -->


## Contact
You can ask questions on Moodle through the Moodle Overflow forum. Please post questions there, so others can see them and share in the discussion. If you have questions which are not of general interest, please don't hesitate to contact us directly, i.e., post a private note on Moodle or email Ryan with Clara cc-ed.

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
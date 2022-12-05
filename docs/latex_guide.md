# Cheat Sheet for `LaTeX` (document class: article)
Documentation of some things that come up a lot when using `LaTeX` in general as a linguist. 

<!-- 1. [Why `LaTeX`](#Why-`LaTeX`-aka-skip-if-you-know-why)
2. [File architecture](#Architecture-and-terminology-tex-sty-and-other-files)
3. [Text Formatting](#Basics-for-writing)
    3.1. [General formatting](#General-formatting)
        3.1.1. [Bold, italic, smallcaps](#Text-formatting)
        3.1.2. [Linebreak](#Forcing-linebreak)
        3.1.3. [Coloured text](#Coloured-text-with-xcolor)
    3.2. [Inserting images](#Images)
    3.3. [Sections and Paragraphs](#Sections-and-paragraphs)
    3.4. [Labels and crossreferencing](#Labels-and-cross-references)
    3.4. [Citing with BibTex](#Citing-with-BibTeX)
        3.4.1.[The natbib package](#The-natbib-package)
4. [Environments](#Environments)
    4.1. [Lists with numbers and bulletpoints](#Ordered--and-unordered-lists)
    4.2. [Numbered Examples](#Example-sentences)
    4.3. [Glossings](#Glossings)
    4.4. [Tables](#Tables)
        4.4.1 [The tabularx package](#Thetabularx-package-and-others)
    4.5. [Syntaxtrees](#Syntax-trees) 
        4.5.1 [Dependency structures](#Dependency-structures)
5. [Customise your own Commands](#Customise-Commands)
6. [Making your own Style files](#Making-your-own-sty-file)
    6.1. [tcolorbox package](#-Using-the-text-color-box-package)  -->
## Why `LaTeX` (aka. skip if you know why)
This documentation of `LaTeX`(pronounced Lah.Tek or Lay.tek) is meant to give a quick intro into the most basic functions that the software offers in order to write papers, make presentations or design posters.`LaTeX` is a software that simplifies using the typesetter program `TeX`. Since every distribution of `TeX` has its own differences, this documentation is based on the beginner friendly tools that the online interface [`overleaf`](https://www.overleaf.com/) offers. There are many benefits to using `LaTeX` instead of `MS Word` or `google docs` etc. which include the arguments that
* `LaTeX` documents are more stable
* `LaTeX` is free
* `LaTeX` is professional

"Stability" here refers to the fact that document formatting in `word` or `powerpoint` easily (and often) face problems with fonts showing incorrectly on some devices, colours not showing properly or graphics being misplaced. 
In a well written `LaTeX` document, **such things generally do not happen**.

When did you last have to draw a graphic with clipart arrows, added a mathematical formula or create a table in word? Was it tedious? Once you know the right commands and packages, using `LaTeX` will be just as - or in my opinion, even less - tedious as that, but the result will be cleaner, more professional and it will even show properly in a pdf.

If you have not written code before, `LaTeX` may seem daunting with its brackets and slashes, but once you learn what they mean, you will see that most the codey parts are actually for making your document prettier, and not actually part of your writing content.

It may interest you that `LaTeX` is used by many contemporary scientists to write their papers and posters. Also, there are a bunch of `LaTeX` templates on `overleaf` which you can use with even the most basic knowledge over the software, so you don't even have to learn how to do things from scratch! The least `LaTeX` users do, anyways.

So without further ado, let's start with the architecture and structure of `LaTeX` documents.

## Architecture and terminology, `.tex`, `.sty` and other files

When you create a document from scratch, the only thing you will see is a file with the `.tex` extension. That file is where you will write all of your content and where you will be altering things most of the time. 

In `overleaf`, a blank `main.tex` file will have some barebone construction that looks like this:

```latex=
\documentclass{article}
\usepackage[utf8]{inputenc}

\title{This is a title}
\author{Anh Kim N.}
\date{December 2022}

\begin{document}

\maketitle

\section{Introduction}

\end{document}
```
There are two important regions to take note of in this:
* The `preamble` (line 1-7)
* The `document` between `\begin{document}` and `\end{document}` (line 8-14)

You can create multiple `.tex` files and distribute your writing among them, too. This is useful if you want to sort your writing eg. chapters or collaborator parts into separate files. This also makes looking things up more easy. 

In order to see what your code is doing, you need to `compile` it. Compiling code in `overleaf` is the equivalent to running a script and seeing if it works, you need to click the download button to actualy save the output file. 

If you decided to use a template, your folder will have other things included, such as a `.sty` file, a `.bib` file, images or even `.pdf` files. Here are some important things to know about this all.

### Preamble
```latex=
\documentclass{article}
\usepackage[utf8]{inputenc}

\title{This is a title}
\author{Anh Kim N.}
\date{December 2022}
```
Metadata information, packages for formatting and customisations are declared in the `preamble`. In graphically elaborate papers, slides and posters, the `preamble` can end up being incredibly long and impossible to read. In order to keep your preamble easy to navigate, try to group packages in a way that seems sensible and make use of comments to keep track of the packages' functions, as their names can range from very intuitive to cryptic. Here an example, of what I mean:

```latex=
% In the preamble
\documentclass{article}

%% Tables and structures
\usepackage{paralist} % Make lists compact
\usepackage{tabularx} % More table options
\usepackage{booktabs} % Horizontal divide lines for tables
\usepackage{array} % Additional table format options
\usepackage{float} % More control over float objects
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Citations
\usepackage{natbib} % More citation options
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Graphical elements
\usepackage{xcolor} % Allow colours
\usepackage{graphicx} % Allow using images
\usepackage{forest} % Drawing syntax trees
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Text formatting
\let\eachwordone=\itshape % First line in examples in italic
```

The word `preamble` also refers to the first lines of an environment, since that is where the options for the environment are set. In this guide, I will mostly use the term to distinguish between where lines of code have to go inside of the entire document, but if you refer to other guides online, please be aware of this fact.

https://olivierpieters.be/blog/2016/08/10/latex-preamble

### Document classes
```latex=
\documentclass{article}
```
LaTeX can be used to create different formats of pdf files. Different classes have different standard layout settings, such as the `letter` class making the addresses of recipient and sender appear at the top of the first page, or the `beamer` class transforming the document into presentation slides. Classes may have class-specific `packages` and `commands` and it can be very confusion to keep track of what is compatible with which class.  

This tutorial will cover only the `article` class, which is the one most popular for academic writing. A guide on `beamer` may follow in the future.

The class is set at the very beginning of the `preamble`
### Packages
```latex=
\usepackage[utf8]{inputenc}
```
Packages are in LaTeX what `libraries` are in other programming languages. While `LaTeX` is not quite a programming language, if you are unfamiliar with the concept of a `library`, you may find this explanation very helpful:

> Any programming language uses predefined `statements` and `commands`  to follow your instructions, which means that you can only use words and concepts _that your program knows_.
> Sometimes, you may find that your programming language does not know the sufficient words to do the things you would like it to do. 
> This is where `libraries` come in: `libraries` are collections of  books that contain new `functions` and `commands`, *new words for your programming language*. When you `import` libraries, you are bringing new books to your programming language and teach it how to do new things.
> <small>My 8th grade Computer teacher</small>

In the above example, we are importing the package `inputenc`, which tells LaTeX which encoding to use to display letters, in this case`[utf8]` . UTF-8 is generally the default encoding, but should you wish to change it, now you now know which package to use.

Packages along with settings for their commands have to be declared in the `preamble`.

### The `document` environment
```latex=
\begin{document}

\maketitle

\section{Introduction}

\end{document}
```
This is where the actual writing is happening. If you are using templates and have a hard time navigating the structure, make sure you find where `\begin{document}` and `\end{document}` are located at least. Any kind of writing which is not included inside of the `document environment` (eg. as a `reference`), will not show up in your final product and is very likely to cause an error if it is not any type of formatting setting.

You will see the command `\maketitle` being used here first. This command is using the information from `\title{This is a title}`,`\author{Anh Kim N.}` and `\date{December 2022}` we have provided in the `preamble`.

This is followed by `\section{Introduction}`, a command that formats the words inside of the `{}` into a section headline, in this case the word "Introduction". More info about sections and paragraphs follow [here](#Sections-and-paragraphs).

You may have noticed that many things are called a 'document'. Where possible, I will try to highlight the word `document` to mean the environment and will simply say document to mean the entire document file that we are writing in the broader sense.

### Style file
### Bibliography

More on bibliography and citing can be found [down below](#Citing-with-BibTeX)

### Errors and Warnings
Once in a while you will run into errors, which may amass to the point of your document failing to compile. 

**Errors** (coloured in red) are things that need urgent addressing and even if you see the pdf compiling, you should fix them. Errors are not just suggestions.

Meanwhile **Warnings** (coloured in orange) are things that can often go ignored, since they will not cause the document to break. Warnings will mostly notify you about unexpected inconsistencies that need addressing (eg. the famous [*overfull hbox warning*](https://tex.stackexchange.com/questions/36767/overfull-hbox-how-do-i-fix-this)) or clashes between packages that attempt to modify the same parameters, but apart from formatting not immediately showing as intended, warnings are ok to ignore.

## Basics for writing

[SOME INFO ON THE STRUCTURE AND THE FILES OF LATEX,]

### Handy shortcuts to get used to
Most of these are common practice and used in other programs, too and infinitively easier to use on a keyboard with English layout. If you want to become a proficient computer user, learning shortcuts is a quick way to make you proficient. Challenge yourself to never using `right-click > copy > paste` ever again.

`ctrl+enter`: compiling
`ctrl+ left-right-arrowkeys`: let's you skip across words
<!--`ctrl+c`: copy selected text
`ctrl+x`: cut out selected text
`ctrl+v`: paste selected text
`ctrl+z`: undo things
`ctrl+y`: undo your undone things -->
`ctrl+/`: comment and un-comment ( whole blocks and lines )
`ctrl+b`: bold ( pastes `/textbf{}`)
`ctrl+i`: italic ( pastes `/textit{}`)
`tab`: indent text ( located on the left side of your keyboard with the two ↹ arrows )
`shift+tab`: unindent
<!--`ctrl+a`: select the entire document -->
`ctrl+f`: search for words
`ctrl+h`: search for words and replace them
`ctrl+u`: selected text to upper case
`ctrl+shift+u`: selected text to lower case

### General formatting
#### Text formatting
In `LaTeX`, formatting commands are initiated with the backslash `\`.
```latex=
\textit{Italic text}, \textbf{Bolded text}

\textit{\textbf{Italic and bolded text}}
```
> *Italic text*, **Bolded text** 
> 
> ***Italic and bolded text***

```latex=
A text in normal size and a \textsc{text in smallcaps}
```
A text in normal size and a <small>TEXT IN SMALLCAPS</small> 

#### Forcing linebreak
`\\` are used to force a linebreak. There are many alternatives
```latex=
This\\ text \linebreak is \newline broken.
```
> This
> text
> is
> broken.

#### Coloured text with `xcolor`
You can also colour your writings and define custom colours to use in themes, if you  use the `xcolor` package:
```latex=
% In the preamble
\usepackage{xcolor}
[ADD EXAMPLE OF CUSTOM DEFINED COLOUR]
```
```latex=
% In the document
\textcolor{red}{This text is in red}
```
> <font color="#FF0000">This text is in red</font>

### Images
[ADD PACKAGE INFO]
```latex=
\includegraphics[scale=.5]{IMG_1934.jpg}
```


### Sections and paragraphs
When you write sections and paragraphs, the following commands allow you to format the headline of the paragraph appropriately. In the `\documentclass{article}`, sections, subsections and sub-sub sections will automatically be indexed as you write and updated in the table of contents, so you won't have to keep track of which numbers you have to rearrange when you decide to swap out or delete sections.

```latex=
% In the document
\section{This is the Introduction} % 1
\subsection{This is a subsection} % 1.1 
\subsubsection{This is a subsubsection} % 1.1.1
\paragraph{This is a paragraph} % bold face with a tab space to the right
```
### Labels and cross references
Whenever you include images, tables or quotes, you may want to refer back to them. Instead of having to describe what you refer to, it is possible to set a `label` for your object:
```latex=
% In the document
\label{MyOwnReference}
```
When you want to refer back to your object inside of your text, simply add this:

```latex=
% In the document
\ref{MyOwnReference}
```
An index should appear in the text. If you want to refer to the page on which the item is located, use:
```latex=
% In the document
\pageref{MyOwnReference}
```
[ADD SECTION ON INCLUDE SECTION FOR REFERRING ACROSS FILES]

### Citing with BibTeX

`LaTeX` uses the `BibTeX` format for saving references. Bib entries take this rough format:
```latex=
% In your .bib file
@article{nguyenA2022,
  title={Cheat Sheet for `LaTeX`},
  author={Nguyen, Anh Kim},
  journal={Shenanigans of the SLaM Lab},
  pages={9999-10000},
  year={2022},
  publisher={SLaM Lab}
}
```

If you are using Overleaf, you should create a file with the `.bib` extension. Whenever you want to include a reference, you should add its `BibTex` information into that `.bib` file. You do not need to sort your references, as ``LaTeX`` will do that for you.

```latex=
% In the preamble
\bibliography{NameOfYourBibFile.bib} 
```
In order to cite these references in your text, you can use `\cite[pageNumber]{NameOfBibReference}`. To cite the bib entry above, you would use:

```latex=
% In the document
\cite[42]{nguyenA2022}
```
This will appear in the text:
> (Nguyen, 2022: 42)

It is possible to leave out the [pageNumber] as for cases such as online sources, conference talks or computer software.

Only cited entries will appear in the "References" section at the end. So it is possible to have more entries in your `.bib` file than what you are using.

#### The `natbib` package
`natbib` is a package that allows for more citation options.
```latex=
% In your preamble
\usepackage{natbib}
```
Choose from a series of different citing styles:

**`citet`** is for citing inside of **text**, so you can refer to authors in the middle of describing their ideas and concepts. If you include an asterisk(`*`) before the `{}`, it will cite all authors who are listed in the `bib`-entry.
```latex=
% In the document
\citet[42]{nguyenA2022} % Nguyen (2022: 42)
```
**`citep`** is for citing with **paranthesis** around the whole citation, which is useful after paragraphs and paraphrases. It also allows you to include additional letters in front of the author's name, such as "cf.", "ibd.", etc. If you include an asterisk(`*`) before the `{}`, it will cite all authors who are listed in the `bib`-entry.
```latex=
% In the document
\citep[cf.][42]{nguyenA2022} %(cf. Nguyen, 2022: 42)
```
**`citealt`** is a plain, **alternative** format of the citation in case you are using special citation guidelines which requires you to use different brackets or hypens.
```latex=
% In the document
\citealt[42]{nguyenA2022} % Nguyen 2022: 42
```
There are also:
```latex=
% In the document
\citeauthor{nguyenA2022} % (Nguyen) 
\citeyear{nguyenA2022}	% (2022)
```

### Full citation in the footnote with the `footbib` package
```latex=
% In the preamble
\usepackage{footbib}
\footbibliographystyle{plain}
\footbibliography{references} 
```


```latex=
% In the document
 \footcite{BibEntry} 
```

## Environments
An environment is a section on a page that will have the same formatting from the environment's `\begin{}` until its `\end{}`. This can take the form of things such as [`item-lists`](#Lists-and-Examples), [`inter-linear glosses`](#Glossings), `tables`, `images`,`textboxes` and many more.

### Ordered- and unordered lists

You can specify bulletpoint shapes in `[]`. The default bulletpoint is a circle. Notice how there is a nested environment in lines `5-7` in order to indent the fourth bullet point.

```latex=
% In the document
\begin{itemize}
    \item[A.] One
    \item[2.] Two
    \item Three
    \begin{itemize}
        \item Four
    \end{itemize}
\end{itemize}
```
Will give you something like this.
> A. One  
> 2. Two  
>・Three  
> * Four  

### Example sentences 

If you have singular items that you want to analyse (eg. an example sentence you want to highlight), the `exe`-environment will automatically count all of the examples you have named up to the moment you use it.
```latex=
% In the document
\begin{exe}
    \ex First example
\end{exe}
The mitochondria is the powerhouse of the cell :)
\begin{exe}
    \ex Second example
    \exi 🐟 Fish example
    \ex Third example
\end{exe}
```
> (1) First example
> 
> The mitochondria is the powerhouse of the cell :)
> 
> (2) Second example
> 🐟　Fish example
> (3) Third example

As you can see `\ex` is the normal command that indexes examples. If you need examples with different indexing or want to name an example that will not be counted, you can use `\exi` followed by a custom index of your choice.

#### Indexing with Roman numbers and alphabet with the `enumitem` package

The `exe`-environment does not have a designated setting for indexing with letters or using roman numbers. Instead, we can use the `enumitem` package which is used like this:

```latex=
% In the preamble
\usepackage{enumitem}

% In the document
\begin{enumerate}[label=(\alph*)]
\item small alphabet letter
\end{enumerate}

\begin{enumerate}[label=(\Alph*)]
\item big alphabet letter
\end{enumerate}

\begin{enumerate}[label=(\roman*)]
\item small roman number
\end{enumerate}

\begin{enumerate}[label=(\Roman*)]
\item big roman number
\end{enumerate}
```
>(a) small alphabet letter
>(A) big alphabet letter
>(i) small roman number
>(I) big roman number



### Glossings and the `gb4e` package
```latex=

```

### Tables
#### `tabular`-environment
On default, `LaTeX` can implement a simple table construction. The most simple construction of `tabular` looks like this:  

```latex=
% In the document
\begin{tabular}{c|c} 
    aa & ab \\
    ba & bb \\
    ca & cb \\
\end{tabular}
```
Table cells are divided by `&` and `\\`.  

The `{c|c}` is the part that specifies the content alignment of the table. every letter specifies one column, so the table above allows has two columns which are divided by a vertical `|`-line. There are multiple ways to align content, using the following letters inside of the `{}` does the following
* `c` - columns are center aligned
* `l` - columns are left aligned
* `r` - colums are right aligned
* `p{4cm}` - content is a paragraph whose text can wrap into the next lines. `{4cm}` can be changed to however long the cell should be

#### The`tabularx` package and others

[ADD EXPLANATION FOR THIS BEFORE YOU FORGET HOW TO USE IT AGAIN]

```latex=
% preamble for the table, how many columns and what kind of columns it will have
\begin{tabular}{ccl>{\raggedright\arraybackslash}p{4cm}} % c = center aligned. l = left aligned, r = right aligned, x = user defined, p = length of the line
     \toprule % creates a line on top with booktabs
     asdsad & cxxx  & aisdhasd & jkashdaiusdh \\
     \midrule % a line in the middle
     akjdhasd &  akjdhajksd & sdsdsdsd & akjdhsjkadghsagdjhkasajdjs adjhsad jhagdjhasgd lkjskldsakldj gdjsa gdjhagd jhkgadd hlakd  \\
     \bottomrule % a line on the bottom
\end{tabular}
```

* `>{}` and `<{}` - additional formatting options for the column that the arrow is pointing to


```latex=

```

### Syntax trees
What would a cheat sheet for linguists be without a section on syntax trees. [LOOK AT BEAMER SLIDES AGAIN]

#### Dependency structures
What would a cheat sheet for linguists be without a section on syntax trees [LOOK AT BEAMER SLIDES AGAIN]

## Customise Commands

### Making your own commands
It's possible to make your own commands for fast formatting or structuring the entire flow of objects in your file. The barebone structure of the line that you need in order to initialise a custom command looks like this:
```latex=
\newcommand\commandname[Argument1][Argument2]{modifications on Argument #1 and #2}
```
in which `\commandname` is the name of the new customised command. The `[] []` are to be filled with numbers which stand for arguments that are being used in the `{}`.


An example use for this would be eg. customised formatting for glosses. We want our interlinear glossing to be displayed in <small>SMALL CAPS</small>, everytime we gloss a part-of-speech:  
```latex=
% In the preamble
\newcommand\gloss[1]{\textsc{#1}}
```
in which the #1 tells the command which argument to modify.  
To use the new gloss command, we use
```latex=
% In the document
\gll   This    is        an        example. \\
       This \gloss{cop} \gloss{det} example. \\
```
You can customise commands as you like! In the following, I want to use the `\gloss` only for glosses that are less frequent and instead define designated glosses for subjects, accusatives and dative. So everytime I use the `\sbj`,`\acc` and `\dat` commands, I want <small>SBJ, ACC, DAT</small> to be pasted into the text, no arguments required:
```latex=
% In the preamble
\newcommand\gloss[1]{\textsc{#1}}
\newcommand\sbj{\textsc{SBJ}}
\newcommand\acc{\textsc{ACC}}
\newcommand\dat{\textsc{DAT}}
```

```latex=
% In the document
\gll   I           give  the        tree       a          kiss. \\
       1.Pers.\sbj give \gloss{det} tree.\dat \gloss{det} kiss.\acc. \\
```
In the compiled pdf, you will see: 

I give the tree a kiss.
1.Pers.<small>SBJ</small> give <small>DET</small> tree.<small>DAT</small> <small>DET</small> kiss.<small>ACC</small>


### Making your own environment
[DUMMY TEXT HOW TO MAKE YOUR OWN ENVIRONMENT, SEE THE STY FILE]

```latex=
\newenvironment{nameOfYourEnvironment}
    {Some formatting like \begin{center}}
    {The same formatting you opened up there \end{center}}
```
If you wish to learn more about this, you can read up on custom [commands](https://www.overleaf.com/learn/latex/Commands#Defining_a_new_command) and [environments](https://www.overleaf.com/learn/latex/Environments#Defining_a_new_environment) on the overleaf documentation.

## Making your own `.sty` file
A `style file` is to the `tex file` what the`CSS stylesheet` is to the `HTML file`.
Avoid typing one up for yourself if you can, but if you **must** create one, I can tell you some packages that I have used up until now. At this point, you do not care about the `overfull hbox` error anymore, but instead ask yourself _"How can I destroy the hbox, these silly borders, I don't need them"_

### ?. Using the `text color box` package
`tcolorbox` or `tcb` is a package that can create a wide range of highly customisable boxes and column environments, which is very useful for creating posters.
```latex=

```
### Author
[Anh Kim Nguyen](https://slam.phil.hhu.de/authors/anh/)  
Many thanks to [Mogens Mastracchio](https://twitter.com/mostracchio) for teaching me how to use LaTeX in the first place.
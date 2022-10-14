# SlaM Lab Website guide
This document describes the process of setting up the website code on your local in order to work on it, as well as the website architecture, mainly in regards to the content. The code can be found in [this repository](https://github.com/hhuslamlab/website). This guide will gradually be extended to include more example workflows and more explanations as needed.  

**It is HIGHLY reccommend** to read through the architecture before you go and change things. It will not take a lot of time but greatly facilitate further work on the website, and help you work on issues not covered in this guide. 

> **_NOTE:_**  This guide is written for linux users. Windows users may experience difficulties and may have to look at alternate commands. 

---
This document helps you to:
- [Set up](#setting-up-the-website-on-your-local)
- [Understand the Website Architecture](#website-architecture) 
    - [Understand Its Widgets](#widgets) 
    - [Menu header - Referencing the widgets](#menu-header)

Example workflows - How to:
- [Change/add author information]() 
- [Change widget information]()
- ---

## :computer: Setting up the website on your local
First, you need to clone the repository using [git](https://git-scm.com/). In your command line interface type: 
```bash
git clone git@github.com:hhuslamlab/website.git
```
Then, follow the instructions in the [README](https://github.com/hhuslamlab/website) of the repository to install [Hugo](https://gohugo.io/) and [Golang](https://gohugo.io/).

## :european_castle: Website Architecture
> **_HINT:_**  For this section it is helpful to have the website open in a different tab and have a look at the elements that are talked about. 

###  Widgets
The website was built using a template called 'academic', that organizes the website in **widgets**. A widget is an element or a section on the website, for example the `People` or `publication` sections. These widgets are referenced in the menu at the top of the page. Clicking on a point in the menu movey you to the corresponding widget on the page. 

#### Types of Widgets 
There are different types of widgets, that is to say, templates which you can copy and use for different content. What a widget can do depends on the content of the widget file. In theory, you can create a widget yourself but using and modifying templates saves a lot of time. 
For example, the widget used for the "people" section display small cards with some extra info, and more additional info if you click on it. Because the purpose of the "academic" website template is what the name suggests, this widget is made for displaying information about people (authors, members, etc.) but can be used for anything else. 
There are other widgets, like the slider-widget, which is like a self-moving presentation, or the talk-widget, which is not currently in use. 

#### Widget files
Lets use the people-widget as an example, to see how the widget files work. Below is the file for the people-widget whcih can be found at `website/content/home/people.md`:
![](https://i.imgur.com/nrCscHE.png)
The file starts with `+++` and ends with three plus signs. This is similar to 
```latex
\begin{document}
...
\end{document}
```

in Latex, and denotes the **beginning and end of the file**. Every line that starts with a `#` sign is a **comment** that will not be visible on the website. 

The top of the file contains important information about the widget. The comment at the top tells us what kind of widget this is and what its intended use-case is. The four lines below are options where we can enable/disable things and set variables. Unless your name is Akhilesh, you will probably never need to touch the firs two options. The third one is pretty straight forward, `true` activates the widget, while setting `false` deactivates it. 
`Weight` is a variable that is linked to the `website/config/_default/menu.toml` file which is responsible for the menu bar on top of the page. (This is explained [here](#change/-add-author-information)) 

This is a widget that does not have its content in the widget file itself, but rather lets you point to a folder where the applicable information is located. This information is set in the `content` bracket `folder = "people"`.

Other options are, as the headings tell you, related to advanced options and styling, which you will probably never have to touch. If you do, the comments will help you, they are pretty obvious imo. 

### Menu header 
The top of the website shows the menu bar which lets you navigate to different elements (widgets) on the page. Which text links to what widget and how they are displayed is set in the `website/config/_default/menu.toml` file:
![](https://i.imgur.com/zydC5Jt.png)
As you can see, some widgets are commented out with a hashtag. That means that we are currently not using this widget. If you wanted to remove a widget from the menu bar, you could either delete it or comment it out. It is always better to comment it out rather than deleting it. Note that this will only remove the widget from the menu bar, not delete the content of the widget on the actual homepage. For that you would have to delete the actual widget file in `website/content/home/`. By commenting out the widget, you merely remove the link to it. 

How the widget is linked is set in the **name parameter**. This does not have to congrue with the actual name of the widget, this can be anything that you want to name the menu point. The crucial part is the **url parameter** below. As is expained at the top of the document, this links to the widget folder we talked about earlier, and shows the path to the corresponsing widget. The widget `events` has a differnt url because it links to a new page. 

Lastly, by setting the **weight parameter**, you designate the order in which the elements appear in the menu bar. The lowest number appears furthest to the left, the highest number appears furthest to the right. In the current website version, we use numbers in steps of ten from 10-100.

### :heavy_check_mark: What to do now?
Most likely, you read this because you want to make some changes to the website. I recommend to start with a sandbox of some kind, where you can safely make changes and try things out. The best way to do this is to go to your local version of the website repository, checkout a new branch and make that branch your playground. If I already lost you at the word GitHub, just ask me (Anna) or Akhilesh to help you out. 

If you already know what you are doing, go forth and prosper :mortar_board:.


## :bust_in_silhouette: Change/ Add author information
### Changing information of an existing auhtor
1. Go to `website/content/authors/`.
2. Pick the author you want to change information of and go to their folder. 
3. Open the file `_index.md`. 
The top of the file should look like this: 
![](https://i.imgur.com/c2bPvzk.png)

- `title` changes the name of a person
- `Social/Academic Networking` contains links for social media and email. 
    - When changing the email, make sure to keep `mailto:` so the mail programm automatically opens when you click the link on the website
    - remove any links that you dont need
    - dont worry about the icons or ask me or Akhilesh

### Adding a new author
1. Go to `website/content/authors/`.
2. Copy an existing folder and rename it. 
    > **_NOTE:_** If you dont know how to naviagte folders, look at the corresponding guide. 
3. Change the corresponding information, see the last heading if you need more info. 

## More to be added

## Authors
[**Anna Stein**](https://slam.phil.hhu.de/authors/anna)

# Jupyter Notebook (WSL and Windows)

This tutorial assumes that you have installed Python. If you don't you can find the guide [here](/Python_setup).


## For WSL

---
Enter the line below in Ubuntu.

```bash
pip install jupyter
```
Open bashrc with the nano editor.
```bash
nano ~/.bashrc
```
Create an alias to be able to start Jupyter Notebook from WSL.
```bash
alias jupyter notebook="~/.local/bin/jupyter-notebook --no-browser"
```
<img title="nano" alt="nano" src="nano.png">

Type `ctrl` + `X` and type `y` and then `enter`. This will take you back to your bash shell.

Launch Jupyter Notebook.
```bash
jupyter notebook
```

The output should look like the picture below. Copy and paste one of the red bracketed links into the browser t open Jupyter Notebook there.

<img title="terminal" alt="terminal" src="terminal.png">

You can terminate the session by clickling `Quit` at the top right in your browser or entering `ctrl` + `y` followed by `y`.


## For Windows
Go to the official [Python website](https://www.python.org/downloads/) and download the appropriate version for your device.

Press the Windows key + 'r' and type cmd to open the command line.

To make sure you have Python installed, type `pip help`.
If you DO NOT get the input below, you are good to go :)

```bash
'pip' is not recognized as an internal or external command, operable program or batch file.
```
If you do get this, follow the quick trouble shooting below.

---
First, we need the version of Python that you have installed: `python --version`.

To add the Python to your PATH variable, type the line below but note, that you need to substitue your Python version. Below is the line for Python 3.9.

```sh
setx PATH "%PATH%; C:\Python39\Scripts
```
---

See above for how to enter Jupyter Notebook.

Happy Coding :)


### More help
If none of this works for you, you can contact one of the authors.

### Authors
[**Anna Stein**](https://slam.phil.hhu.de/authors/anna/)
[**Akhilesh Kakolu Ramarao**](https://slam.phil.hhu.de/authors/akhilseh/)

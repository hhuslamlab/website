# Jupyter Notebook

This tutorial assumes that you have installed Python. If you don't you can find the guide [here](/Python_setup).

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

Happy Coding :)


### More help
If none of this works for you, you can contact one of the authors. 

### Authors
[**Anna Stein**](https://slam.phil.hhu.de/authors/anna/)
[**Akhilesh Kakolu Ramarao**](https://slam.phil.hhu.de/authors/akhilseh/)

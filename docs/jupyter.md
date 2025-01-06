# Jupyter notebook

- [Jupyter Notebook](#installing-jupyter-notebook)
    - [R Kernel for Jupyter notebook](#r-kernel-for-jupyter-notebook)

## Installing Jupyter Notebook
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

```shell
setx PATH "%PATH%; C:\Python39\Scripts
```
To start Jupyter Notebook, type `jupyter notebook` and press enter.
    
### R Kernel for Jupyter Notebook
Install the system dependencies:
```shell
sudo apt-get -y build-dep libcurl14-gnutls-dev
sudo apt-get install libcurl14-openssl-dev libssl-dev
sudo apt-get install -y zlib1g-dev libssh2-1-dev libpq-dev libxm12-dev
sudo apt-get build-dep libxml2-dev
sudo apt install build-essential libcurl14-gnutls-dev libxml2-dev libssl-dev
sudo apt-get install libx11-xcb1
sudo apt-get install qtbase5-dev qtchooser qt5-qmake atbase5-dev-tools
```

Install r-base
```bash
sudo apt install r-base r-base-dev
```

Start R by entering`R`.
Install the IRKernel
```bash
install.packages("IRKernel",repos="https://cran-rstudio.com/")
```
---
You might run into errors such that the program is unable to fetch the packages. In this case you will have to install the package separately, ignoring the version number. To do so, press `ctrl`+ `c` to terminate the installation process and install the package. Below is an example, where the installation of the utf8 package is not working:

```sh
trying URL 'https://cloud.r-project.org/src/contrib/utf8_1.2.2.tar.gz'
```
`ctrl` + `c`
```sh 
install.packages("utf8", repos="https://cran.rstudio.com")
```
---
Continue with the line below.
```R
IRKernel::installspec(user=FALSE)
```



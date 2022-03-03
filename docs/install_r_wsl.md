# Working with R in Jupyter Notebook (WSL & Ubuntu)

## Installation

### Windows Sub-system Linux (WSL)

### R


```sh
sudo apt r-base r-base-dev
```

### System dependencies

```sh
sudo apt-get -y build-dep libcurl4-gnutls-dev
sudo apt-get install libcurl4-openssl-dev libssl-dev
sudo apt-get install -y zlib1g-dev libssh2-1-dev libpq-dev libxml2-dev
sudo apt-get build-dep libxml2-dev
sudo apt install build-essential libcurl4-gnutls-dev libxml2-dev libssl-dev
sudo apt-get install libx11-xcb1
sudo apt-get install qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools
```

### R packages

Installing IRKernel --

```R
install.packages("IRKernel", repos = "https://cran.rstudio.com/")
```

You might run into errors such that the program is unable to fetch the packages, in which case you will have to install the package separately (press `Ctrl+C` to terminate the installation process).

Please disregard the version number (example: utf8_1.2.2, use only utf8) while installing individual packages.

Here's an example of the above case, in which the package `utf8` is not working --

Output trace:

```R
trying URL 'https://cloud.r-project.org/src/contrib/utf8_1.2.2.tar.gz'.
```
Try installing `utf8` using --

```R
install.packages("utf8", repos = "https://cran.rstudio.com/")
```

This is just an example for `utf8` and can happen with any package you try.

The same error might appear when you are installing the individual (example, `utf8`) package, in which case, you have to run the install.packages command again (`Ctrl+C` and run the above command again). This is likely due to the internet connection or due to the network drivers.


### IRKernel

```R
IRkernel::installspec(user=FALSE)
```

## Running

### R

Open R session in the terminal using `R` command. Additionally, you might want to consider running `R` with `sudo` using `sudo -i R`.

### Jupyter Notebook

```sh
jupyter notebook
```

Click on `R` under `New` when you open the jupyter notebook to initate the R Kernel.

### Support

Please feel free to contact [Akhilesh](mailto:kakolura@hhu.de), if you need any support regarding this tutorial.

### Authors

[**Anna Stein**](https://www.linkedin.com/in/anna-stein-20bb42196/)

[**Akhilesh Kakolu Ramarao**](https://slam.phil.hhu.de/authors/akhilesh/)

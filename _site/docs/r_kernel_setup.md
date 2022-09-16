# R Kernel for Jupyter Notebook (WSL2)

## 
Install the system dependencies
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
sudo apt r-base r-base-dev
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

## More help<a name="help"></a>
If have more questions that the internet can't answer, you can contact Akhilesh.

### Authors
[**Anna Stein**](https://slam.phil.hhu.de/authors/anna/)
[**Akhilesh Kakolu Ramarao**](https://slam.phil.hhu.de/authors/akhilseh/)

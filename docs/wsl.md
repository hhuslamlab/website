# WSL2
The Windows Subsystem for Linux enables you to run a GNU/Linux environment on Windows, without a virtual machine or dualboot setup. WSL2 also runs a Linux Kernel.


This guide will help you install WSL2 and show you some basic folder structure navigation. You can also learn how to setup other software on WSL2, like Python, R, Jupyter Notebook and more. 

---
- [Install WSL2](#installing-wsl2)
    - [Setup](#setup)
    - [Error solving](#error-solving)
- [The command line interface](#the-command-line-interface) 
    - [Navigating directories](#navigating-directories)
    - [Interacting with files](#interacting-with-files)
        - [Accessing Windows files on WSL](#accessing-windows-files-on-wsl)
    - [Overview of basic commands](#overview-of-basic-commands)
- [Python](#installing-python) 
- [Docker engine](#installing-docker-engine)
    - [Docker compose](#installing-docker-compose)
    - [Using Docker](#using-docker)
        - [Uploading images to DockerHub](#uploading-images-to-dockerhub)
- [Jupyter Notebook](#installing-jupyter-notebook)
    - [R Kernel for Jupyter notebook](#r-kernel-for-jupyter-notebook)
- [Snaps](#installing-snaps)
- [Java](#installing-java)
- ---

## Installing WSL2
Click the Windows logo on the bottom left of your home screen and search for `Turn Windows features on or off`.
Check the box on `Virtual Machine Platform` and `Windows Subsystem for Linux`. You will then be asked to restart your device.

Click on the Windows logo again and search for `command prompt`. Then right-click on it and select `open as administrator`.

Type the line below in the command prompt.
```shell
wsl --install
```

After that is done, follow this link and click on `WSL2 Linux kernel update package for x64 machines` to download: https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package 


Download Ubuntu from the Microsoft store, that is an app on your laptop. After the download is complete, start Ubuntu as an administrator. If you encounter an error, you can skip to ['Error Solving'](#error-solving) below.

### Setup
You'll be asked to create a **password** and **username**. The password will be hidden when you type it, just press enter when you have finished typing. You will be asked to repeat your password. After that, update your Ubuntu with the lines below.

```bash
sudo apt update
sudo apt upgrade
``` 
### Error solving 
You might encounter an error saying that virtualization options are not enabled. In that case, you have to change some setting this in your **BIOS**:

Turn your computer off. When you click the button to turn it back on, immediately spam the `esc` button to get to the startup menu. This might be a different key depending on your laptop, you can google how to get to your bios if `esc` doesnt work. You know that it worked when you see a black screen with some text on it.

:warning: **Proceed with caution!** :warning:
This part of the guide varies for each laptop and its build. Doing something wrong in the BIOS can break your laptop. Ask one people for help if you are unsure what you are doing. 

The option to enable virtualization is most likely in the `Advanced settings` under `CPU options`, `processor`, `Northbridge` or `Chipset`. There is most likely an `acceleration section` which has a virtualization option which needs to be set to `enabled`. Use `f10` or any other save-changes-button to exit the BIOS and restart your laptop. 

https://filestore.community.support.microsoft.com/api/images/0851b216-07d2-4a85-ad47-bbcc6c0bc206?upload=true

## The command line interface
- [Navigating directories](#navigatin-files/directories)
- [Interacting with files](#interacting-with-files)
    - [Accessing Windows files from WSL2](#accessing-windows-files-from-wsl2)
- [Overview of basic commands](#overview-of-basic-commands)

### Navigating directories
You can think of the command line as a different way to interact with your laptop, it just has less buttons that do things automatically.

For example, if you want to look at the files in a certain folder (a directory), you would click on the folder and it would show you the folders and files contained inside. You can do this in the commandline as well, by using `ls` (go try it out!). 

<img title="website_directories "src="/assets/terminal_neutral.jpg">

The colors indicate what each item is. Most importantly, blue items are folders, white items are files. 

If you want to change directories, you can use the command `cd` (=change directory) followed by the name of the directory. Here is an example of this and other useful `cd` commands: 

```sh
# Go to the content folder. 
cd content

# Go to the home folder inside of the content folder. 
cd content/home/

# Go back to the previous directory in the current directory path
cd ..

# Go to the home directory
cd ~
```

To get the path of your current directory, you can type `pwd`. 

If the name of the directory is distinct enough, meaning there are no other items that have the same characters you typed so far, you can **autocomplete** what you are writing with the `tab` button (Also try that out!). This also works for file names etc. 

### Interacting with files
- `cp filename destination/path` copies the file to the destination path given
- `cat filename` prints the file content
- Checkout [this guide](https://akkikek.xyz/tutorials/vim/index.html) on deeper, more practical file interaction with **vim**.
- `rm filename` removes a file, add the `-r` flag to remove directories

 **Note:** The filename always includes the file extension.
 

### Accessing Windows files from WSL2 
Go into the root directory.
```bash
cd /
```
Now change into your Windows directory.
```bash
cd mnt
```
Type cd followed by the file path. The path has to fullfill the following requirements:
- written with single forward slashes
- no quotation marks
- beginning with `c` or `d` depending on your file system

Below is an example of a path navigating to some secret files.
```bash
cd c/Users/Name/Documents/secret_files
```

#### Overview of basic commands
```sh
# List the current directory contents
ls

# Get the path of the current directory
pwd

# Go to the content folder. 
cd content

# Go to the home folder inside of the content folder. 
cd content/home/

# Go back to the previous directory in the current directory path
cd ..

# Go to the home directory
cd ~

# Clear your screen
clear
```

### Misc
- `clear` will clear your screen
- `up arrow` lets you re-use previous commands
- `tab` is like autocompletion for filenames, paths, ...

## Installing Python
First, check whether Python is installed.

``` bash
python3
```

If you see something like below, you already have Python installed. Type `exit()` to exit python and continue your setup journey with a different tutorial :)

```bash
Python 3.8.10 (default, date, time)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

If you do not, you can install Python by entering the line below. Adding `ipython3` automatically installs the Python Kernel for Jupyter notebook.
```bash
sudo apt install python3 python3-pip ipython3
```

To confirm your installation, type python3 again. You should now see something like mentioned above.  

## Installing Docker engine

Follow <a href="https://docs.docker.com/engine/install/ubuntu/">this guide</a> in the official Docker documentation starting from the heading "Install using the repository".
After you have installed Docker, the guide asks you to run a "Hello World" Docker image with the following command.

```bash
sudo docker run hello-world
```
You might get the error below.
```bash
docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?.
See 'docker run --help'.
```
To fix it, you can first run the command:
```bash
sudo service --status-all
```
The sign next to "docker" should be either `?`or `-`. Then run the next command to start docker.
``` bash
sudo service docker start
```
Retry the "Hello World" image from above, it should work now. The output looks something like this:
```bash
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
2db29710123e: Pull complete
Digest: sha256:10d7d58d5ebd2a652f4d93fdd86da8f265f5318c6a73cc5b6a9798ff6d2b2e67
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

### Installing Docker compose

Follow <a href="https://docs.docker.com/compose/cli-command/#install-on-linux">this guide<a> using only the section under the headline "Install on Linux".
    
## Using Docker
- **Docker image:** like a zip file that contains the software setup
- **Docker container:** an instance of the image that is not persistent, nothing will be saved
- **Docker volume:** a way of mounting a local directory to the container for itneracting with the container (.yml file is a config. file for loading the right image and mounting the volume)


### Uploading images to DockerHub
DockerHub contains many docker images that are created by others. It is useful for building on existing images, e.g. specific versions of Ubuntu. Conceptually, it is similar to GitHub. Docker images can be shared to DockerHub, however importing existing images may be dangerous, since they may come from malicious users.

**Step 1:** Create your own Docker image
In order to do this, we have to create a text file called 'Dockerfile' - no extension needed. Here is an example for setting up the prerequisites for WaveGAN:

``` shell
FROM ubuntu:18.04
RUN apt update
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install python3.9 -y
RUN apt install wget -y
RUN apt install python3-pip -y

RUN python3 -m pip install cpython
RUN python3 -m pip install scipy==1.0.0
RUN python3 -m pip install matplotlib==3.0.2

RUN apt install llvm-9 -y
RUN ln -s /usr/bin/llvm-config-9 /usr/bin/llvm-config
RUN LLVM_CONFIG=/usr/bin/llvm-config-9
RUN python3 -m pip install llvmlite --user
RUN python3 -m pip install librosa==0.6.2

RUN python3 -m pip install tensorflow-gpu==1.12.0
RUN apt install git -y
RUN git clone https://github.com/chrisdonahue/wavegan.git wavegan_v2
```

The lines are similar to standard Ubuntu installation lines - except for:
1. `RUN` is needed for all lines, except for importing images
2. Prefix `pip instal` with `pyhton3 -m`
3. Suffix `apt install` with `-y` to 'yes' all the prompts

``` shell
ubuntu: 18.04
```

Note that the name of the docker image to import from DockerHub can be found on [DockerHub](https://hub.docker.com/) - you would need to look under 'View Available Tag' and search for the right version.

**Step 2:** Check what images there are:

```sh
sudo docker images
```

**Step 3:** Create an instance of the image
```shell
sudo docker run -it <NAME:TAG>
```

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

    
## Installing Snaps
In Ubuntu type:
```bash
sudo apt-get update && sudo apt-get install -yqq daemonize dbus-user-session fontconfig
```

```bash
sudo daemonize /usr/bin/unshare --fork --pid --mount-proc /lib/systemd/systemd --system-unit=basic.target
```

```bash
exec sudo nsenter -t $(pidof systemd) -a su - $LOGNAME
```

To check if the installation worked, run `snap version`. The output should look something like below:
```bash
snap    2.54.3+20.04.1ubuntu0.3
snapd   2.54.3+20.04.1ubuntu0.3
series  16
ubuntu  20.04
kernel  5.10.102.1-microsoft-standard-WSL2
```
---
If at any point you encounter an error like this: 
`sudo: daemonize: command not found` it means you have to install the daemonize package. 
```shell
sudo apt-get install daemonize
```
Run the command that errored out again and it should work.
    
## Installing Java
Check whether Java is already installed:
```bash
java -version
```

### Installing OpenJDK JRE
```bash 
sudo apt install default-jre
```
Run the comman `java -version` to see if the installation worked.
You should see something like the output below.
```bash
openjdk version "11.0.11" 2021-04-20
OpenJDK Runtime Environment (build 11.0.11+9-Ubuntu-0ubuntu2)
OpenJDK 64-Bit Server VM (build 11.0.11+9-Ubuntu-0ubuntu2, mixed mode)
```

### Installing Oracle HotSpot JRE
First, you need to download the JRE binaries. You need to make sure to download the right file. On the webtie linked below, you can find it under the heading **JRE 8**, which is NOT the first heading you see on the website. Currently the file is called `jre-8u333-linux-x64.tar.gz` and the 'Product/file description' is `x64 Compressed Archive`.
You can find the website [here](https://www.oracle.com/java/technologies/downloads/#java8).

---

Create a directory to install JRE with:
```bash 
sudo mkdir /usr/local/java
```

Move the JRE binaries into the directory:
```bash
sudo mv jre-8u291-linux-x64.tar.gz /usr/local/java
```

Go to the install directory:
```bash
cd /usr/local/java
```

Unpack the tarball (the .tar file):
```bash
sudo tar zxvf jre-8u291-linux-x64.tar.gz
```

To save space, delete the tarball by running:
```bash
sudo rm jre-8u291-linux-x64.tar.gz
```

Let the system know where JRE is installed: 
```bash
sudo update-alternatives --install "/usr/bin/java" "java" "/usr/local/java/jre1.8.0_291/bin/java" 1
```
If this errors out, you need to check which version you have and change the number in `jrel. ....` like below.  

---

Go to the directory with `cd /usr/local/java` and list the content with `ls`. 
You should see something like this: `jre1.8.0_333`, though your numbers might be different. 
Run `sudo` command from above again but replace the `jrel. ....` part with what was in your directory. 

---

Make sure that the installation worked by running `java -version`. The ouput should look something like this: 
```bash
java version "1.8.0_291"
Java(TM) SE Runtime Environment (build 1.8.0_291-b10)
Java HotSpot(TM) 64-Bit Server VM (build 25.291-b10, mixed mode)
```

### Setting the Java home variable 
Check if the Java developer kit is installed with `javac --version`.
If not, you need to install it with 
```bash
sudo apt install default-jdk
```
Get the location of the Java compiler on your computer:
```bash
which javac
```
The output you get will probably look like this: `/us/bin/javac`. I will be using this path for the rest of the tutorial but if you got a different path as an output, use the one that you got. 

---

```bash
ls -l /usr/bin/javac
```
You should get some colorful output that contains an arrow. 

```bash
readlink -f `which javac``| sed "s:/bin/javac::"
```

Set the Java home variable with the path that you recieve as output from above.

```bash
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

Check if it worked with `echo $JAVA_HOME`, you should see your path.

At this point, the variable is only temporary, meaning when you close your terminal window, the variable disappears. Let's make it permanent.

```bash
echo "export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64" >> ~/.bashrc

#Check if it worked
tail -3 ~/.bashrc
```
You should see your JAVA_HOME variable in the last line of your output. 

## Authors
[**Anna Stein**](https://slam.phil.hhu.de/authors/anna/)

[**Akhilesh**](https://slam.phil.hhu.de/authors/akhilesh/)

<<<<<<< HEAD
# website

## Installation

### Linux (ubuntu-based distros) and WSL

Install Hugo and the Go language

``` sh

sudo apt install hugo
sudo apt install golang

```
#### Run hugo server
Check if Hugo is installed
```sh
hugo version 
```
You should see something like the line below.
```sh
Hugo Static Site Generator v0.68.3/extended linux/amd64 BuildDate: 2020-03-25T06:15:45Z
```

Generate ssh keys
```sh
ssh-keygen -t rsa -b 2048 -C <"your_email@example.com">
```
For the prompt just press enter, the file will be generated and saved automatically.
Keep pressing enter until you are back at the command line.

```sh
cat ~/.ssh/id_rsa.pub
```
Copy the hash. Go to your Github profile settings and click on SSH and GPG key. Create a new SSH key with with a title of your choosing. 
Paste the hash under "key" and click add SSH key. 

Clone the website
```sh
git clone git@github.com:hhuslamlab/website.git
```
```sh
cd website
```
```sh
hugo server
```

### MacOS

Install brew 

``` sh

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

Install Hugo and Go language 

``` sh

sudo apt install hugo
sudo apt install golang

```


## Building

``` sh

hugo

```

## Running

``` sh

hugo server

```


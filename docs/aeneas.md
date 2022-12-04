# Installing Aeneas on WSL and MacOS
This is a detailed guide to install Aeneas (https://github.com/akki2825/aeneas) that supports python3.6+ on Windows Subsystem for Linux (WSL) and MacOS.

# Windows Subsystem for Linux (WSL)
If you dont have WSL yet you can install it with [this guide](https://docs.slam.phil.hhu.de/#/wsl).
Once you do run: 
```sh
sudo apt-get update
sudo apt-get upgrade
```

## Easy Installation
Download the script from here (https://gist.github.com/akki2825/3b38a9f33170b31617b141e53745565b) and run this shell script using:
```sh
git clone https://gist.github.com/akki2825/3b38a9f33170b31617b141e53745565b
cd 3b38a9f33170b31617b141e53745565b/
sh install_py3_aeneas.sh
```

## Detailed Installation
Clone the py3-aeneas repository
```sh
git clone https://github.com/akki2825/aeneas
cd aeneas/
```

### Install system dependencies
```sh
sudo apt-get install -y python3-dev
sudo apt-get install python3-pip
sudo apt-get install make autoconf automake libtool pkg-config
sudo apt-get install libespeak-dev
sudo apt-get install ffmpeg
sudo apt-get install espeak
sudo apt-get install espeak-data
```

### Install Python packages
```sh
sudo pip3 install numpy
sudo pip3 install py3-aeneas
```

### Compile Python C/C++ extensions

sudo python3 setup.py build_ext --inplace
Check Setup
```sh
sudo python3 -m aeneas.diagnostics
```

# MacOS
Copy and Paste the below code in the terminal (using Command+C and Command+V):

## Install Brew
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## Easy Installation
Download the script from [here](https://gist.github.com/akki2825/8014a2800eaf638eee2989974655c98f) and run this shell script using:

```sh
git clone https://gist.github.com/akki2825/8014a2800eaf638eee2989974655c98f
cd 8014a2800eaf638eee2989974655c98f/
sh install_py3_aeneas.sh
```

## Detailed installation
### Clone the py3-aeneas repository

```sh
git clone https://github.com/akki2825/aeneas
cd aeneas/
```

### Install system dependencies

```sh
brew install python3
brew install python3-dev
brew install python3-pip
brew install ffmpeg
brew install espeak
brew install espeak-data
```

### Install Python packages

```sh
sudo pip3 install numpy
sudo pip3 install py3-aeneas
```

### Compile Python C/C++ extensions

```sh
sudo python3 setup.py build_ext --inplace
```

### Check Setup
```sh
sudo python3 -m aeneas.diagnostics
```

## Authors
[**Akhilesh**](https://slam.phil.hhu.de/authors/akhilesh/)

# WSL2

The Windows Subsystem for Linux enables you to run a GNU/Linux environment on Windows, without a virtual machine or dualboot setup. WSL2 also runs a Linux Kernel.

This guide will help you install WSL2 and show you some basic folder structure navigation using the command line interface.

---
- [Install WSL2](#installing-wsl2)
    - [Setup](#setup)
    - [Error solving](#error-solving)
- [The command line interface](#the-command-line-interface) 
- [Navigating directories](#navigating-directories)
- [Interacting with files](#interacting-with-files)
    - [Accessing Windows files on WSL](#accessing-windows-files-on-wsl)
- [Overview of basic commands](#overview-of-basic-commands)
---

## Installing WSL2

Click the Windows logo on the bottom left of your home screen and search for `Turn Windows features on or off`.
Check the box on `Virtual Machine Platform` and `Windows Subsystem for Linux`. You will then be asked to restart your device.

Click on the Windows logo again and search for `command prompt`. Then right-click on it and select `open as administrator`.

Type the line below in the command prompt.
```shell
wsl --install
```

After that is done, follow this link and click on `WSL2 Linux kernel update package for x64 machines` to download: https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package 


Download Ubuntu from the Microsoft store, that is an app on your laptop. **Choose version 20.4.** After the download is complete, start Ubuntu as an administrator. If you encounter an error, you can skip to ['Error Solving'](#error-solving) below.

## Update WSL

Download the update from here: [https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)

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
cd ~/
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

## Authors

[**Anna Stein**](https://slam.phil.hhu.de/authors/anna/)

[**Akhilesh**](https://slam.phil.hhu.de/authors/akhilesh/)

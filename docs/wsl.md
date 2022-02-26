# Opening files from Windows on WSL:  

**A few general notes**
Use the command `ls` to list the content of your working directory, the folder that you are currently 'in'. The command `cd` is used to change directory to one that you specify after the command in the same line by typing the path of that directory.   

---
Open Ubuntu by searching for it and clicking on the icon.  
In Ubuntu, change to your root directory by typing the line below

``` bash
cd ../..
```

In the new line, the `~$` from your first line, should now be replaced by `~$`  .

You can also type `ls` and hit enter, to see if you are in the right directory. It should look similar to this:   

![](https://codimd.c3d2.de/uploads/1cda57d3a061176525c231b18.png)

Now change into your Windows directory by typing
``` shell
cd mnt
```

Again, you should see this change in the blue part of your new line:   
![](https://codimd.c3d2.de/uploads/1cda57d3a061176525c231b19.png)


To finally change to the directory your desired file is in, type `cd` followed by the file path. The path has to fullfill the following requirements: 
- written with single forward slashes 
- no quotation marks
- beginning with `c` or `d` depending on your drive

Below is an example: 

``` bash
cd c/Users/Name/Documents
```

After navigating into your desired folder you can open the file by typing 

``` bash
wslview <filename.type>
```
(replace the variable with your filename, no brackets)

You can also use the line below to open your working directory in your file explorer.

``` bash
wslview . 
```

# Copying files to WSL directory from Windows

Open Ubuntu by searching for it and clicking on the icon. 

**Step 1:** Go to relevant directory
``` bash
cd /mnt/c/yourpath
```
Replace `yourpath` with the directory that the file that you want to copy is in. 

**Step 2:** Copy the file
``` bash
cp <filename> ~/
```
Replace `<filename>` with the name of your file like so: 'examplefile.pdf'. 
The '`~/`' copies the file to the home directory of your wsl. If you want to copy it to a different directory, enter the name of the directory after the forward slash. There is an example below: 
``` bash
cp <filename> ~/directoryName
```

You can check if it worked by changing to the directory and listing its content.
``` bash
cd ~/ 
```
``` bash
ls
```

### Authors

[**Anna Stein**](https://www.linkedin.com/in/anna-stein-20bb42196/)



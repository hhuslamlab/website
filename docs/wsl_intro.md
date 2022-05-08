# WSL2
## Table of Contents
[Navigating directories](#files)
[Accessing Windows files from WSL2](#mnt)
[Interacting with file](#vim)
[More help](#help)


## Navigating directories <a name="files"></a> 
-  `cd path/to/somehwere` changes into the directory you provide (example: `cd documents` or `cd documents/secrets`)
-  `cd ~` will get you back to the home directory from anywhere
- `ls` will list the contents of the directory that you are currenty in
- `cd ..` will take you back on directory, not time- but path-wise 

## Accessing Windows files from WSL2 <a name="mnt"></a>
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

## Interacting with files <a name="vim"></a>
- `cp filename destination/path` copies the file to the destination path given 
- `cat filename` prints the file content
- Checkout [this guide](https://akkikek.xyz/tutorials/vim/index.html) on deeper, more practical file interaction with **vim**. 
- `rm filename` removes a file, add the `-r` flag to remove directories

 **Note:** The filename always includes the file extension.

## Misc
- `clear` will clear your screen
- `up arrow` lets you re-use previous commands 
- `tab` is like autocompletion for filenames, paths, ..

## More help<a name="help"></a>
If have more questions that the internet can't answer, you can contact one of the authors.

### Authors
[**Anna Stein**](https://slam.phil.hhu.de/authors/anna/)
[**Akhilesh Kakolu Ramarao**](https://slam.phil.hhu.de/authors/akhilseh/)

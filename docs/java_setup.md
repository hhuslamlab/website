# Java (WSL2)
Check whether Java is already installed:
```bash
java -version
```

---

## Installing OpenJDK JRE
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

## Installing Oracle HotSpot JRE
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

## Sources
[Oracle](https://www.oracle.com/java/technologies/downloads/#java8)

[phoenixNAP](https://phoenixnap.com/kb/check-java-version-linux)


## Authors
[**Anna Stein**](https://slam.phil.hhu.de/authors/anna/)



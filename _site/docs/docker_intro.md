# .. Docker (WSL2)

## Docker concepts:
- Docker image: like a zip file that contains the software setup
- Docker container: an instance of the image that is not persistent, nothing will be saved
- Docker volume: a way of mounting a local directory to the container for itneracting with the container (.yml file is a config. file for loading the right image and mounting the volume)


## Uploading images to DockerHub
DockerHub contains many docker images that are created by others. It is useful for building on existing images, e.g. specific versions of Ubuntu. Conceptually, it is similar to GitHub. Docker images can be shared to DockerHub, however importing existing images may be dangerous, since they may come from malicious users.

---

This section presupposes that you have installed Docker. If you don't you can find a tutorial [here](/docker_setup).

---


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

**Step 2:** Check what images there are
``` shell
sudo docker images
````

**Step 3:** Create an instance of the image
```shell
sudo docker run -it <NAME:TAG>
```

### References
[https://docs.docker.com/storage/volumes/](https://docs.docker.com/storage/volumes/)

### Authors

[**Prof. Dr. Kevin Tang**](https://slam.phil.hhu.de/authors/kevin/)

[**Anna Stein**](https://slam.phil.hhu.de/authors/anna/)

# A starter guide to Docker engine

- [Docker engine](#installing-docker-engine)
    - [Docker compose](#installing-docker-compose)
    - [Using Docker](#using-docker)
        - [Uploading images to DockerHub](#uploading-images-to-dockerhub)

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


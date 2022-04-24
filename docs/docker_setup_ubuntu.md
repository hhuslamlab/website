# Setting up Docker on Ubuntu

## Installing Docker engine

Follow <a href="https://docs.docker.com/engine/install/ubuntu/">this guide<a> in the official Docker documentation starting from the heading "Install using the repository".
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

## Installing Docker compose

Follow <a href="https://docs.docker.com/compose/cli-command/#install-on-linux">this guide<a> using only the section under the headline "Install on Linux".

### Authors
[**Anna Stein**](https://www.linkedin.com/in/anna-stein-20bb42196/)

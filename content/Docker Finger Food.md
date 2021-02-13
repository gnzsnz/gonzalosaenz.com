Title: Docker Finger Food
Date: 2020-03-19
Modified: 2021-02-13
Category: Misc
Tags: docker
Slug: Docker Finger Food
Authors: Gonzalo Saenz
Status: published
Summary: This post cover bits and pieces of docker. I plan to update it as I go.

# Docker Finger Food

Below you will find docker finger food. This is and will always be a work in progress post.

<!-- TOC -->

- [Use an APT proxy from a container](#use-an-apt-proxy-from-a-container)
- [Delete dangling images](#delete-dangling-images)
- [Don't install apt recommends](#dont-install-apt-recommends)
- [Non interactive apt](#non-interactive-apt)
- [Clean up your apt cache](#clean-up-your-apt-cache)
- [Clean up your pip cache](#clean-up-your-pip-cache)
- [Manager application logs](#app-logs)
- [Docker build](#docker-build)
- [Docker run](#docker-run)
- [Docker exec](#docker-exec)
- [Docker prune](#docker-prune)
- [Docker useradd](#docker-useradd)
- [Docker config](#docker-config)

<!-- /TOC -->

## Use an APT proxy from a container <a name="use-an-apt-proxy-from-a-container"></a>

If you are not using an APT proxy you should. If you are, then you will find this useful.

In your ´Dockerfile´

```sh
ARG APT_PROXY
RUN echo 'Acquire::http { Proxy "http:'$APT_PROXY'"; }'  \
    | tee /etc/apt/apt.conf.d/01proxy \
    apt-get update -y && apt-get -y install ...
```

Then, when you build your docker image,
```sh
docker build \
  --build-arg APT_PROXY="http://apt-cacher:3142" -t you/image .
```

Credit --> [run apt-get with proxy in Dockerfile](https://stackoverflow.com/questions/48749200/run-apt-get-with-proxy-in-dockerfile). To install your apt-cacher container you can try [this one](https://github.com/sameersbn/docker-apt-cacher-ng), or [this other one](https://github.com/menghan/docker-image-apt-cacher-ng), our just build your own.

## Delete dangling images <a name="delete-dangling-images"></a>

As you work with your Dockerfile to build your dream image you will generate dangling images in the process. We all do it. This will help you,

```sh
docker rmi $(docker images -q --filter "dangling=true")
```

Credit -->[Dangling images](https://takacsmark.com/dockerfile-tutorial-by-example-dockerfile-best-practices-2018/#dangling-images)

## Don't install apt recommends <a name="dont-install-apt-recommends"></a>

In your `Dockerfile`
```sh
RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
  ca-certificates \
  wget
```
The magic is done by `--no-install-recommends`parameter.

## Non interactive apt <a name="non-interactive-apt"></a>

Another trick to consider is to use `DEBIAN_FRONTEND=noninteractive` as part of the `RUN`line as the preferred option. It is not recommended to use `ENV DEBIAN_FRONTEND=noninteractive` --> [Source](https://github.com/moby/moby/issues/4032).

## Clean up your apt cache <a name="clean-up-your-apt-cache"></a>

You don't want to keep your .deb files in your docker image. So you delete them once your dependencies have been installed.

```sh
RUN apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
  rm -rf /var/lib/apt/lists/*
```

## Clean up your pip cache <a name="clean-up-your-pip-cache"></a>
 In the same way that we don't want to keep .deb files in our docker image, we should not bloat it with python packages
```sh
RUN python -m pip install --no-cache-dir --upgrade pip \
  pip install --no-cache-dir request
```
## Manage application logs <a name="app-logs"></a>

In this section I will go through the steps to set up the JSON logging driver. There are multiple options to setup logging drivers, please see reference below.

First you need to setup the docker daemon logging. To do this you need to edit the `/etc/docker/daemon.json` which is the default location for linux systems. 

```json
{
  "log-driver": "json-file",
  "log-level": "info",
  "log-opts": {
    "max-size": "5m",
    "max-file": "5",
  	"compress": "true"
    "mode": "non-blocking"
    "max-buffer-size": "4m"
  }
}
```

This is telling the docker daemon to user json-file as logging driver, max log file size 5MB, i till rotate logs and keep 5 files, and will use compression for rotated files.

Once he `daemon.json` file is updated, you need to restart dockerd. Any new container  will use these settings. All the previously created containers will use previous settings (most probably default settings.)

Another aspect to configure is the log delivery mode from the container to the log driver

```sh
docker run -it --log-opt mode=non-blocking --log-opt max-buffer-size=4m ubuntu tail -f /var/log/syslog
```

The command above is using the `non-blocking` mode which is NOT the default, and using buffer of 4MB. The `non-blocking` mode stores log messages in an intermediate per-container ring buffer for consumption by driver. While `direct` is blocking and delivers directly to the driver.

In docker-compose you would do:

```yaml
version: "3.9"
services:
  some-service:
    image: some-service
    logging:
      driver: "json-file"
      options:
        max-size: "5m"
        max-file: "5"
        compress: "true",
    		mode: "non-blocking",
    		max-buffer-size": "4m"
```



Reference:

* [Docker daemon logging](https://docs.docker.com/config/containers/logging/configure/)
* [JSON logging driver](https://docs.docker.com/config/containers/logging/json-file/)
* [Docker compose logging]()

## Docker build <a name="docker-build"></a>

Docker build cheat-sheet

```sh
docker build -t user/image .
```
`-t` parameter will set the image name in the user/image fashion. This is telling docker to build an image based on the Dockerfile in the current directory ".".

## Docker run <a name="docker-run"></a>


```sh
# fresh ubuntu
docker run -ti --name bionic ubuntu:latest

```

## Docker exec <a name="docker-exec"></a>

Docker exec cheat-sheet.

```sh
docker exec -ti  --user container_user container_name bash
```

This will run in interactive mode (-ti) under container_user (the user in the container) on container container_name, bash.

## Docker prune <a name="docker-prune"></a>

This is a continuation of section [Delete dangling images](#delete-dangling-images). The prune command will help you to keep your host clean. As you with Docker containers, images, volumes and more will start to pile up.

```sh
# to clean up images not used by any container - BE CAREFUL
docker image prune

# to clean up stopped containers - BE CAREFUL
docker container prune

# to clean up unused volumes - not attached to a container - BE CAREFUL
docker volume prune
```

## Docker useradd <a name="docker-useradd"></a>

To manage container user and uid/gid is tricky. There are different alternatives, like using the `--user` parameter. However this is not dealing with containers `/etc/passwd` so your container user will be homeless and `whoami` will not work. So usually I try to solve the problem at build time. See below

```sh
ARG USER
ARG USER_ID=1000
ARG USER_GID=1000
ARG BASEPATH=/opt/app
RUN groupadd --gid "${USER_GID}" "${USER}" && \
  useradd -ms /bin/bash --uid ${USER_ID} --gid ${USER_GID} ${USER} &&\
  echo "${USER} ALL=(ALL) NOPASSWD:ALL" | tee -a /etc/sudoers &&\
  mkdir ${BASEPATH} && chown ${USER}:${USER} -R ${BASEPATH}

WORKDIR ${BASEPATH}
USER ${USER}
COPY --chown=${USER}:${USER} . .
```

This will create a user based on environment variables passed at build time. And set the permissions on the image filesystem.

```sh
docker build -t user/image \
--build-arg USER=username \
--build-arg USER_ID=$(id -u username) \
--build-arg USER_GID=$(id -g username) \
.
```

Then when you run the containers

```sh
docker run -it container_name

# to use current user
docker run -it container_name
```
In docker compose

```yaml
# This is an example
version: '3.3'
services:
  app:
  	build:
  		context: .
      args:
        USER: $USER
        USER_ID: $USER_ID
        USER_GID: $USER_GID
    image: user/image:tag
    container_name: "container"
```

This will require an `.env` file in the working directory.

````sh
USER=dockeruser
USER_ID=1000
USER_GID=1000
````

Then run composer like this,

```sh
docker-compose up
```

When I'm working on top of an existing build, for example for PostgreSQL, I would build my image

```sh
FROM postgres:last
ARG UID
ARG GID
ARG OLD_UID
ARG OLD_GID
RUN usermod -u $UID postgres && \
		groupmod -g $GID postgres && \
		find / -group $OLD_GID -exec chgrp -h postgres {} && \
		find / -user $OLD_UID -exec chown -h postgres {}

```

This will keep the postgres user name within the container, and align the uid and gid with the host filesystem.

**References**:

* [Understanding how uid and gid work in Docker containers](Understanding how uid and gid work in Docker containers), 
* [How to add users to a container](https://stackoverflow.com/questions/27701930/add-user-to-docker-container)
* [How to Change a USER and GROUP ID on Linux For All Owned Files](https://www.cyberciti.biz/faq/linux-change-user-group-uid-gid-for-all-owned-files/)


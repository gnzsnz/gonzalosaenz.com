Title: Docker Finger Food
Date: 2020-03-19
Modified: 2020-04-12
Category: Misc
Tags: docker
Slug: Docker Finger Food
Authors: Gonzalo Saenz
Status: published
Summary: This post cover bits and pieces of docker. I plan to update it as I go.

# Docker Finger Food

Below you will find docker finger food. This is and will always be work in progress.

<!-- TOC -->

- [Use an APT proxy from a container](#use-an-apt-proxy-from-a-container)
- [Delete dangling images](#delete-dangling-images)
- [Don't install apt recommends](#dont-install-apt-recommends)
- [Non interactive apt](#non-interactive-apt)
- [Clean up your apt cache](#clean-up-your-apt-cache)
- [Clean up your pip cache](#clean-up-your-pip-cache)
- [Docker build](#docker-build)
- [Docker run](#docker-run)
- [Docker exec](#docker-exec)
- [Docker prune](#docker-prune)
- [Docker useradd](#docker-useradd)

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
## Manage application logs

WIP

## Docker build <a name="docker-build"></a>

Docker build cheat-sheet

```sh
docker build -t user/image .
```
`-t`parameter will set the image name in the user/image fashion. This is telling docker to build an image based on the Dockerfile in the current directory ".".

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

[Source](https://stackoverflow.com/questions/27701930/add-user-to-docker-container)
```sh
RUN useradd -rm -d /home/ubuntu -s /bin/bash -G sudo -u 1000 ubuntu
USER ubuntu
WORKDIR /home/ubuntu
```

Then when you run the containers
```sh
docker run -it --user dockworker:dockworker container_name

# to use current user
docker run -it --user $(id -u):$(id -g) container_name
```
In docker compose

```yaml
# This is an example
version: '3.3'
services:
  app:
    image: user/image:tag
  user: ${UID}
```

Then run composer like this,
```sh
UID=$(id -u):$(id -g) docker-compose up
```

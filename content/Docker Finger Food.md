Title: Docker Finger Food
Date: 2020-03-19
Modified: 2020-03-19
Category: misc
Tags: docker
Slug: Docker Finger Food
Authors: Gonzalo Saenz
Status: draft
Summary: This post cover bits and pieces of docker. I plan to update it as I go.

# Docker Finger Food

Below you will find docker finger food. This is and will always be work in progress.

<!-- TOC -->

- [Docker Finger Food](#docker-finger-food)
  - [Use an APT proxy from a container](#use-an-apt-proxy-from-a-container)
  - [Delete dangling images](#delete-dangling-images)
  - [Don't install apt ecommends](#dont-install-apt-ecommends)
  - [Non interactive apt](#non-interactive-apt)
  - [Clean up your apt cache](#clean-up-your-apt-cache)
  - [Clean up your pip cache](#clean-up-your-pip-cache)
  - [Docker build](#docker-build)
  - [Docker run](#docker-run)
  - [Docker exec](#docker-exec)
  - [Docker prune](#docker-prune)

<!-- /TOC -->

## Use an APT proxy from a container

If you are not using an APT proxy you should. If you are, then you will find this usefull.

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

## Delete dangling images

As you work with your Dockerfile to build your dream image you will generate dangling images in the process. We all do it. This will help you,

```sh
docker rmi $(docker images -q --filter "dangling=true")
```

Credit -->[Dangling images](https://takacsmark.com/dockerfile-tutorial-by-example-dockerfile-best-practices-2018/#dangling-images)

## Don't install apt ecommends

In your `Dockerfile`
```sh
RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
  ca-certificates \
  wget
```
The magic is done by `--no-install-recommends`parameter.

## Non interactive apt

Another trick to consider is to use `DEBIAN_FRONTEND=noninteractive` as part of the `RUN`line as the prefered option. It is not recomended to use `ENV DEBIAN_FRONTEND=noninteractive` --> [Source](https://github.com/moby/moby/issues/4032).

## Clean up your apt cache
You don't want to keep your .deb files in your docker image. So you delete them once your dependencies have been installed.

```sh
RUN apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
  rm -rf /var/lib/apt/lists/*
```

## Clean up your pip cache
 In the same way that we don't want to keep .deb files in our docker image, we should not bloat it with python packages
```sh
RUN python -m pip install --no-cache-dir --upgrade pip \
  pip intall --no-cache-dir request
```


## Docker build

## Docker run

## Docker exec

## Docker prune

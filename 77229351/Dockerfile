FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
        command-not-found \
        software-properties-common \
        coreutils \
        build-essential \
        pkg-config \
        xdg-user-dirs \
        libgl1-mesa-dev \
        freeglut3-dev \
        mesa-utils \
        libvulkan-dev \
        libglfw3-dev \
        libglew-dev \
        xvfb && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /root

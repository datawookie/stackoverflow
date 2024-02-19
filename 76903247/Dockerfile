FROM nvidia/cuda:12.3.1-devel-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y &&\
    apt-get install -y \
        build-essential \
        pkg-config \
        libswscale-dev \
        libpq-dev \
        libxine2-dev \
        libglew-dev \
        zlib1g-dev \
        libpostproc-dev \
        libswscale-dev \
        libeigen3-dev \
        libtbb-dev \
        libgtk2.0-dev \
        python3-pip \
        python3-dev \
        python3-numpy \
        # Install OpenCV here!
        libopencv-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04

ENV NVIDIA_VISIBLE_DEVICES ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

ARG UID=1000
ARG GID=1000

RUN echo "Acquire::GzipIndexes \"false\"; Acquire::CompressionTypes::Order:: \"gz\";" > /etc/apt/apt.conf.d/docker-gzip-indexes
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
        sudo \
        less \
        emacs \
        tmux \
        bash-completion \
        command-not-found \
        software-properties-common \
        curl \
        wget \
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
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y

WORKDIR /root

# COPY square.cpp .

# RUN g++ -std=c++11 square.cpp -o square -lGL -lGLU -lGLEW -lglut -lglfw

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
        git \
        xdg-user-dirs \
        libgl1-mesa-dev \
        freeglut3-dev \
        mesa-utils \
        vulkan-tools \
        libvulkan-dev \
        libglfw3-dev \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# ENV USERNAME cudagl
# ENV HOME /home/$USERNAME
# RUN useradd -m $USERNAME && \
#         echo "$USERNAME:$USERNAME" | chpasswd && \
#         usermod --shell /bin/bash $USERNAME && \
#         usermod -aG sudo $USERNAME && \
#         mkdir /etc/sudoers.d && \
#         echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/$USERNAME && \
#         chmod 0440 /etc/sudoers.d/$USERNAME && \
#         usermod  --uid $UID $USERNAME && \
#         groupmod --gid $GID $USERNAME

RUN apt-get update && \
    apt-get install -y \
        libglew-dev

# USER $USERNAME
# WORKDIR /home/$USERNAME

WORKDIR /root

# COPY square.cpp .

# RUN g++ -std=c++11 square.cpp -o square -lGL -lGLU -lGLEW -lglut -lglfw

FROM tensorflow/tensorflow:1.14.0-gpu-py3

ENV TZ="America/Los_Angeles"
ARG DEBIAN_FRONTEND=noninteractive
RUN rm /etc/apt/sources.list.d/cuda.list && \
    rm /etc/apt/sources.list.d/nvidia-ml.list && \
    apt-key del 7fa2af80 && \
    apt-get update && apt-get install -y --no-install-recommends wget && \
    wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-keyring_1.0-1_all.deb && \
    dpkg -i cuda-keyring_1.0-1_all.deb && \
    apt-get update
RUN apt-get install -y git python3-opencv
RUN mkdir /build
COPY baselines/ /build/baselines
WORKDIR /build/baselines
RUN ls -lrt /build
RUN ls -lrt /build/baselines
RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install -e . -vvv

FROM nvidia/cuda:11.8.0-base-ubuntu22.04

RUN apt-get update && apt-get install -y wget && \
    wget -q https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh && \
    bash Anaconda3-2020.11-Linux-x86_64.sh -b && \
    rm Anaconda3-2020.11-Linux-x86_64.sh

ENV PATH /root/anaconda3/bin:$PATH

# Python packages for testing.
#
RUN conda install -y -q numba cudatoolkit

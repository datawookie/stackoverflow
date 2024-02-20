FROM python:3.7.17

ENV TZ="America/Los_Angeles"
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-key del 7fa2af80 && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        wget \
        git \
        mpich \
        patchelf \
        libopenmpi-dev \
        libglew-dev \
        libosmesa6-dev \
        libgl1-mesa-glx \
        libgl1-mesa-dev \
        libglfw3

RUN mkdir ~/.mujoco

# Add to end of ~/.bashrc.
RUN echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/root/.mujoco/mjpro150/bin' >> ~/.bashrc

RUN wget -q https://www.roboti.us/download/mjpro150_linux.zip
RUN unzip mjpro150_linux.zip -d ~/.mujoco/

# MuJoCo License
#
# 1. If you have a MuJoCo license then copy onto image.
# COPY mjkey.txt /root/.mujoco/mjkey.txt
# 2. Otherwise just download directly.
RUN wget -q https://www.roboti.us/file/mjkey.txt -P ~/.mujoco/

RUN git clone https://github.com/Silvicek/baselines.git /build

WORKDIR /build

RUN pip3 install -e .

# Remove from end of ~/.bashrc.
RUN sed -i '$ d' ~/.bashrc

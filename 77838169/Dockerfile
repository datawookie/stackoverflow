# FROM tensorflow/tensorflow:1.14.0-gpu-py3
# FROM tensorflow/tensorflow:1.15.5-gpu-py3

FROM python:3.7.17

ENV TZ="America/Los_Angeles"
ARG DEBIAN_FRONTEND=noninteractive

# RUN rm /etc/apt/sources.list.d/cuda.list && \
#     rm /etc/apt/sources.list.d/nvidia-ml.list && \

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

#     wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-keyring_1.0-1_all.deb && \
#     dpkg -i cuda-keyring_1.0-1_all.deb && \
#     apt-get update && \
#     apt-get install -y -qq git mpich libglew-dev

# RUN wget https://mujoco.org/download/mujoco210-linux-x86_64.tar.gz
RUN mkdir ~/.mujoco
# RUN tar -xvf mujoco210-linux-x86_64.tar.gz -C ~/.mujoco/

RUN echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/root/.mujoco/mjpro150/bin' >> ~/.bashrc
    # echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/nvidia' >> ~/.bashrc && \
    # echo 'export PATH="$LD_LIBRARY_PATH:$PATH"' >> ~/.bashrc

    # echo 'export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so' >> ~/.bashrc

RUN wget -q https://www.roboti.us/download/mjpro150_linux.zip
RUN unzip mjpro150_linux.zip -d ~/.mujoco/

# MIGHT WANT TO RESTORE LD_LIBRARY_PATH.
# MIGHT WANT TO RESTORE LD_LIBRARY_PATH.
# MIGHT WANT TO RESTORE LD_LIBRARY_PATH.

# MuJoCo License
#
# 1. If you have a MuJoCo license then copy onto image.
# COPY mjkey.txt /root/.mujoco/mjkey.txt
# 2. Otherwise just download directly.
RUN wget -q https://www.roboti.us/file/mjkey.txt -P ~/.mujoco/

# RUN pip3 install cffi==1.15.1 Cython==3.0.8 lockfile==0.12.2

RUN git clone https://github.com/Silvicek/baselines.git /build

WORKDIR /build

# # RUN echo -e "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/root/.mujoco/mjpro150/bin" >>~/.bashrc

# # # # RUN ls -lrt /build
# # # # RUN ls -lrt /build/baselines
# # # RUN pip3 install --upgrade pip setuptools wheel
# # # # RUN pip3 install -e .

# # RUN pip3 install python3-opencv

RUN pip3 install cffi
RUN pip3 install lockfile
RUN pip3 install "Cython<3"
RUN pip3 install numpy==1.21.0
# RUN pip3 install mujoco-py==1.50.1.68

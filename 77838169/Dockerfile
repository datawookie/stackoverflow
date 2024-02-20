FROM tensorflow/tensorflow:1.14.0-gpu-py3

ENV TZ="America/Los_Angeles"
ARG DEBIAN_FRONTEND=noninteractive

RUN rm /etc/apt/sources.list.d/cuda.list && \
    rm /etc/apt/sources.list.d/nvidia-ml.list && \
    apt-key del 7fa2af80 && \
    apt-get update && apt-get install -y --no-install-recommends wget && \
    wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-keyring_1.0-1_all.deb && \
    dpkg -i cuda-keyring_1.0-1_all.deb && \
    apt-get update && \
    apt-get install -y -qq git python3-opencv mpich libglew-dev

# RUN wget https://mujoco.org/download/mujoco210-linux-x86_64.tar.gz
RUN mkdir ~/.mujoco
# RUN tar -xvf mujoco210-linux-x86_64.tar.gz -C ~/.mujoco/

# RUN echo -e 'export LD_LIBRARY_PATH=/home/user-name/.mujoco/mujoco210/bin \
# export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/nvidia \
# export PATH="$LD_LIBRARY_PATH:$PATH" \
# export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so' >> ~/.bashrc

RUN wget https://www.roboti.us/download/mjpro150_linux.zip
RUN unzip mjpro150_linux.zip -d ~/.mujoco/

RUN git clone https://github.com/Silvicek/baselines.git /build

WORKDIR /build

COPY mjkey.txt /root/.mujoco/mjkey.txt

# RUN ls -lrt /build
# RUN ls -lrt /build/baselines
RUN pip3 install --upgrade pip setuptools wheel
# RUN pip3 install -e .

RUN echo -e "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/root/.mujoco/mjpro150/bin" >>~/.bashrc

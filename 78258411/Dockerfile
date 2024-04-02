FROM nvcr.io/nvidia/pytorch:22.12-py3
# 24.03-py3: cuda version 12.4
# FROM nvcr.io/nvidia/pytorch:24.03-py3

# Define variables
ENV PROJECT_NAME mov
ENV PYTHON_VER 3.10
ENV ROOT_PASSWORD 11111
# Create a non-root user
ENV USER_NAME=user
ARG USER_PASSWORD=$ROOT_PASSWORD

# /home/$USER_NAME/anaconda3
ENV CONDA_DIR /home/$USER_NAME/anaconda3

# Install some packages
RUN apt update
# Change the download server
# COPY sources.list /etc/apt/sources.list
RUN apt update

RUN apt install -y wget sudo git
# Timezone pre-setting for other installation if they ask the timezone
ENV DEBIAN_FRONTEND=noninteractive
RUN apt install -y tzdata
RUN ln -fs /usr/share/zoneinfo/Asia/Seoul /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata
# Base
RUN apt install -y build-essential vim screen
RUN apt install -y libgl1-mesa-glx ffmpeg libsm6 libxext6
# For Anaconda
RUN apt install -y libegl1-mesa libxrandr2 libxrandr2
RUN apt install -y libxss1 libxcursor1 libxcomposite1
RUN apt install -y libasound2 libxi6
RUN apt install -y libxtst6 libglib2.0-0

# User setting with password
RUN adduser --disabled-password --gecos "" $USER_NAME  \
    && echo "$USER_NAME:$USER_PASSWORD" | chpasswd \
    && adduser $USER_NAME sudo \
    && echo "$USER_NAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER $USER_NAME

# Set the working directory
WORKDIR /home/$USER_NAME/workspace
# Copy your application code into the container
# COPY ./moving_ai /home/$USER_NAME/workspace

# Install anaconda
RUN sudo wget https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh -O anaconda.sh
RUN sudo chmod +x anaconda.sh
RUN ./anaconda.sh -b -p $CONDA_DIR
RUN sudo rm anaconda.sh
RUN sudo apt clean
RUN sudo rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Update conda, create a new environment, and install OpenCV
RUN $CONDA_DIR/bin/conda update -n base -c defaults conda
RUN $CONDA_DIR/bin/conda create -n $PROJECT_NAME python=$PYTHON_VER
RUN $CONDA_DIR/bin/conda init

# Set the environment variable for Anaconda installation
ENV PATH $CONDA_DIR/bin:$PATH

# Reload the .bashrc file
# To load base conda
RUN /bin/bash -c "source ~/.bashrc || true"

# activate conda
RUN echo "conda activate $PROJECT_NAME" >> ~/.bashrc
RUN /bin/bash -c "source ~/.bashrc || true"

RUN /bin/bash -c "source activate $PROJECT_NAME && \
    pip install Flask-Cors jupyter wandb opencv-python chardet pandas matplotlib scikit-learn flask bcrypt pymysql seaborn"

# Install PyTorch
RUN /bin/bash -c "source activate $PROJECT_NAME && \
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118"


# Copy your application code into the container
# COPY ./requirements.txt /home/$USER_NAME/workspace

# Install any needed dependencies specified in requirements.txt
# RUN /bin/bash -c "source activate $PROJECT_NAME && \
#     pip install --no-cache-dir -r requirements.txt"


# After pytorch
RUN /bin/bash -c "source activate $PROJECT_NAME && \
    pip install torcheval efficientnet_pytorch paramiko"

# Copy the files and set permissions/ownership in a single step
# COPY --chown=$USER_NAME:$USER_NAME ./moving_ai /home/$USER_NAME/workspace/moving_ai


# Install dependencies and run unit tests
# RUN test -d /home/$USER_NAME/workspace/moving_ai/DINO/models/dino/ops && \
#     rm -rf /home/$USER_NAME/workspace/moving_ai/DINO/models/dino/ops || true
# RUN cd /home/$USER_NAME/workspace/moving_ai && \
#     cp -r dino_ops/ops DINO/models/dino/ops

RUN cd /usr/local/cuda
# Verify environment variables
RUN echo "CUDA_HOME: $CUDA_HOME"
RUN echo "PROJECT_NAME: $PROJECT_NAME"
RUN echo "USER_NAME: $USER_NAME"
# To load environment variables
RUN /bin/bash -c "source ~/.bashrc || true"

# Run
# RUN $CONDA_DIR/bin/activate mov && \
#     cd /home/$USER_NAME/workspace/moving_ai && \
#     cd DINO/models/dino/ops && \
#     python setup.py build install

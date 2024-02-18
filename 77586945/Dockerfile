FROM ubuntu:22.04

WORKDIR /root

RUN apt-get update && apt-get install -y \
  software-properties-common \
  build-essential \
  cmake \
  git \
  libssl-dev \
  wget \
  python3 \
  libgmp-dev \
  sudo

RUN apt install -y -qq libgtest-dev && \
    cd /usr/src/gtest && \
    cmake CMakeLists.txt && \
    make && \
    cp ./lib/*.a /usr/lib

RUN wget https://raw.githubusercontent.com/emp-toolkit/emp-readme/master/scripts/install.py && \
    python3 install.py -install --tool --ot --sh2pc --ag2pc && \
    ldconfig && \
    rm -rf *

RUN git clone https://github.com/evilpoke/ppsat.git

WORKDIR /root/ppsat

RUN git checkout 3d4d44bb561d422200ed90841065e90f3ed33875
RUN cmake .
RUN make

RUN cd test && ./runTests.sh

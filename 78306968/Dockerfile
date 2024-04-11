FROM rust:1-bookworm AS builder

RUN apt-get update && \
    apt-get install -y \
        build-essential \
        wget \
        libgmp-dev \
        libmpfr-dev \
        libmpc-dev && \
    rm -rf /var/lib/apt/lists/*

RUN wget -q https://ftp.gnu.org/gnu/gcc/gcc-13.2.0/gcc-13.2.0.tar.gz
RUN tar -xf gcc-13.2.0.tar.gz && \
    cd gcc-13.2.0 && \
    ./contrib/download_prerequisites

# This will cross-compile using the existing GCC on the image.
RUN cd gcc-13.2.0 && \
    ./configure --disable-multilib --enable-languages=c,c++ && \
    make -j$(nproc) && \
    make install

RUN update-alternatives \
        --install /usr/bin/gcc gcc /usr/local/bin/gcc 60 \
        --slave /usr/bin/g++ g++ /usr/local/bin/g++ && \
    rm -rf gcc-13.2.0.tar.gz gcc-13.2.0 && \
    apt purge -y gcc cpp

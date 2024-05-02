ARG UBUNTU_VERSION=20.04
FROM ubuntu:${UBUNTU_VERSION}

ARG COMPILER_VERSION=10
ARG PETSC_VERSION=v3.18.6

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y \
        software-properties-common \
        gnupg \
        wget \
        lsb-release
RUN add-apt-repository ppa:ubuntu-toolchain-r/test

# For recent CMake version.
#
RUN wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc | gpg --dearmor - | tee /usr/share/keyrings/kitware-archive-keyring.gpg >/dev/null
RUN echo "deb [signed-by=/usr/share/keyrings/kitware-archive-keyring.gpg] https://apt.kitware.com/ubuntu $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/kitware.list

RUN apt-get update
RUN apt-get install -y \
        gcc-${COMPILER_VERSION} \
        g++-${COMPILER_VERSION} \
        gfortran-${COMPILER_VERSION} \
        build-essential \
        git \
        python3 \
        openssh-server \
        openssh-client \
        python3-pip \
        ffmpeg \
        libsm6 \
        libxext6 \
        cmake \
        pkg-config \
        openmpi-bin \
        libopenmpi-dev

RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-${COMPILER_VERSION} 60 && \
    update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-${COMPILER_VERSION} 60 && \
    update-alternatives --install /usr/bin/gfortran gfortran /usr/bin/gfortran-${COMPILER_VERSION} 60

RUN python3 -m pip install pytest numpy h5py pathlib requests pandas matplotlib plotly scikit-learn PyYAML Pillow vtk types-PyYAML pytest-cov

RUN echo "Using PETSC_VERSION: ${PETSC_VERSION}"
RUN git clone -b ${PETSC_VERSION} https://gitlab.com/petsc/petsc.git /petsc && \
    cd /petsc && \
    ./configure \
        PETSC_ARCH=linux-gnu \
        --with-fc=gfortran --with-cc=gcc --with-cxx=g++ \
        --with-fortran-bindings \
        --download-openmpi \
        --with-mpi-f90module-visibility=1 \
        --download-fftw \
        --download-hdf5 \
        --download-hdf5-fortran-bindings \
        --download-fblaslapack \
        --download-scalapack \
        --download-ml \
        --download-zlib && \
    make all

ENV PETSC_DIR /petsc
ENV PETSC_ARCH linux-gnu

ENV OMPI_ALLOW_RUN_AS_ROOT 1
ENV OMPI_ALLOW_RUN_AS_ROOT_CONFIRM 1

FROM ubuntu:24.04 as builder

WORKDIR /workspace

RUN apt-get update && apt-get install -y \
    libc6-dev-armhf-cross \
    libstdc++-10-dev-armhf-cross \
    linux-libc-dev-armhf-cross\
    python3 \
    python3-dev \
    python3-venv \
    python3-pip \
    build-essential \
    cmake \
    ninja-build \
    libopenblas-dev \
    wget \
    curl \
    ca-certificates \
    git \
    pkg-config \
    libatlas-base-dev \
    gfortran

# Update CA certificates
RUN update-ca-certificates

# Create a virtual environment and activate it
# RUN python3 -m venv /workspace/venv
# ENV PATH="/workspace/venv/bin:$PATH"

# Now, use Python and Pip from the virtual environment:
# RUN python -m pip install --upgrade pip
RUN pip install numpy Cython

# Set up environment variables for the compiler and qemu
ENV QEMU_EXECVE=1
COPY --from=multiarch/qemu-user-static:x86_64-aarch64 /usr/bin/qemu-aarch64-static /usr/bin/

# Download and install the ARMv7 toolchain (Linaro)
RUN wget --no-check-certificate https://releases.linaro.org/components/toolchain/binaries/latest-7/arm-linux-gnueabihf/gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabihf.tar.xz && \
    tar -xJf gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabihf.tar.xz -C /opt/ && \
    mv /opt/gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabihf /opt/gcc-linaro
# ENV PATH="/opt/gcc-linaro/bin:${PATH}"
# ENV CMAKE_C_COMPILER="/opt/gcc-linaro/bin/arm-linux-gnueabihf-gcc"
# ENV CMAKE_CXX_COMPILER="/opt/gcc-linaro/bin/arm-linux-gnueabihf-g++"

# # Clone ONNX Runtime specific version
# RUN git clone --recursive https://github.com/microsoft/onnxruntime.git && \
#     cd onnxruntime && \
#     git checkout v1.17.0 && \
#     git submodule update --init --recursive

# # Set up the toolchain cmake file
# RUN echo "SET(CMAKE_SYSTEM_NAME Linux)\n\
# SET(CMAKE_SYSTEM_VERSION 1)\n\
# SET(CMAKE_C_COMPILER arm-linux-gnueabihf-gcc)\n\
# SET(CMAKE_CXX_COMPILER arm-linux-gnueabihf-g++)\n\
# SET(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)\n\
# SET(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)\n\
# SET(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)\n\
# SET(CMAKE_FIND_ROOT_PATH_MODE_PACKAGE ONLY)\n" > /workspace/onnxruntime/tool.cmake

# # Build ONNX Runtime
# WORKDIR /workspace/onnxruntime
# RUN ./build.sh --config Release --allow_running_as_root --update \
#     --build --parallel --build_shared_lib \
#     --cmake_extra_defines CMAKE_TOOLCHAIN_FILE=/workspace/onnxruntime/tool.cmake


# # Set up final image
# FROM arm32v7/ubuntu:24.04
# COPY --from=builder /workspace/onnxruntime/build/Linux/Release /usr/local/lib/onnxruntime

# # Set environment variables
# ENV LD_LIBRARY_PATH=/usr/local/lib/onnxruntime/lib:$LD_LIBRARY_PATH

# # Set work directory
# WORKDIR /data

# # Entry command
# CMD ["bash"]

FROM ubuntu:22.04

RUN apt-get update -q && \
    apt-get install -y -qq git cmake g++

RUN export MY_INSTALL_DIR=$HOME/.local
RUN git clone --recurse-submodules --depth 1 --shallow-submodules https://github.com/grpc/grpc
WORKDIR /grpc
RUN mkdir -p cmake/build
WORKDIR /grpc
RUN cmake -DgRPC_INSTALL=ON -DgRPC_BUILD_TESTS=OFF -DCMAKE_INSTALL_PREFIX=$MY_INSTALL_DIR && \
    make -j 4 && \
    make install

WORKDIR /

COPY run_unittests.sh run_unittests.sh
RUN chmod +x run_unittests.sh

COPY CMakePresets.json CMakePresets.json
COPY get_grpc.cmake get_grpc.cmake
COPY get_dependencies.cmake get_dependencies.cmake
COPY CMakeLists.txt CMakeLists.txt
COPY src src

WORKDIR /build
ARG BUILD_VERSION="0.0.0"
ARG PYTHON_EXECUTABLE="/opt/python/cp310-cp310/bin/python"

RUN cmake .. \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DIGRAPH_INSTALL=ON \
    -DGEOS_INSTALL=ON

# # cmake .. --preset debug_linux -DBUILD_VERSION="0.0.0" -DPython_EXECUTABLE="/opt/python/cp310-cp310/bin/python"

# RUN cmake .. --preset debug_linux -DBUILD_VERSION=${BUILD_VERSION} -DPython_EXECUTABLE=${PYTHON_EXECUTABLE}
# WORKDIR /build/Debug
# # RUN cmake --build . --target routinglib_unittests

# # Run code coverage
# WORKDIR /
# RUN ./run_unittests.sh

# WORKDIR /build
# # Build python package
# # RUN cmake .. --preset release_linux -DBUILD_VERSION=${BUILD_VERSION} -DPython_EXECUTABLE=${PYTHON_EXECUTABLE}
# WORKDIR /build/Release
# # RUN cmake --build . --target python_package
# WORKDIR /build/Release/src/RoutingPython/dist
# # RUN auditwheel repair WeatherRouting-0.0.0-cp310-cp1310-linux_x86_64.whl

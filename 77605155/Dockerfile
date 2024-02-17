FROM nvcr.io/nvidia/tensorrt:21.06-py3

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -q && \
    apt-get install -y -qq \
        g++ \
        libglfw3-dev \
        libstb-dev \
        xvfb

COPY facewarp.cpp .
RUN g++ -I/usr/include/stb/ facewarp.cpp -lGL -lglfw -o facewarp

ENV DISPLAY=:99

ENTRYPOINT []
CMD Xvfb :99 -screen 0 1024x768x16 & ./facewarp

FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
        build-essential \
        cmake \
        python3-pip \
        pkg-config \
        libegl-mesa0 \
        libegl1-mesa \
        libegl1-mesa-dev \
        libgl1-mesa-dev \
        libglu1-mesa \
        libglu1-mesa-dev \
        libgl1-mesa-dri \
        libgl1-mesa-glx \
        libglapi-mesa \
        libgles2-mesa \
        libgles2-mesa-dev \
        libglw1-mesa \
        libglw1-mesa-dev \
        libglx-mesa0 \
        libosmesa6 \
        libosmesa6-dev \
        libfreetype6-dev \
        mesa-utils \
        xdotool \
        mesa-common-dev \
        libglib2.0-0 \
        xvfb \
        x11-xkb-utils \
        xfonts-100dpi \
        xfonts-75dpi \
        xfonts-scalable \
        xfonts-cyrillic \
        xorg \
        openbox \
        xserver-xorg-core

RUN pip3 install conan && conan profile detect

ENV XVFB_WHD="1920x1080x24"\
  DISPLAY=":99" \
  LIBGL_DEBUG="verbose" \
  LIBGL_ALWAYS_SOFTWARE="1" \
  MESA_DEBUG="1" \
  GALLIUM_DRIVER="llvmpipe" \
  LP_NO_RAST="false" \
  LP_DEBUG="" \
  LP_PERF="" \
  LP_NUM_THREADS=""

COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

# Suppress warning messages about missing files.
#
RUN echo "<driconf></driconf>" >/etc/drirc && \
    ln -s /etc/drirc /root/.drirc

ADD * /opt/glcrash/
RUN cd /opt/glcrash && \
    mkdir build && \
    cd build \
    && conan install .. --build missing --output-folder=. -s build_type=Debug -c tools.system.package_manager:mode=install \
    && cmake .. -DCMAKE_TOOLCHAIN_FILE=build/Debug/generators/conan_toolchain.cmake -DCMAKE_POLICY_DEFAULT_CMP0091=NEW -DCMAKE_BUILD_TYPE=Debug \
    && cmake --build .

FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y \
        wget \
        curl \
        git \
        unzip \
        build-essential \
        python3 \
        libglx-dev libopengl0 libuv1-dev

RUN curl -sL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y \
        nodejs

RUN git clone https://github.com/klokantech/tileserver-gl.git /tileserver-gl

WORKDIR /tileserver-gl

RUN npm install
RUN npm install -g npm@10.5.0 tileserver-gl

WORKDIR /

RUN wget https://github.com/maptiler/tileserver-gl/releases/download/v1.3.0/zurich_switzerland.mbtiles

EXPOSE 8080
ENV PORT 8080

CMD tileserver-gl --file zurich_switzerland.mbtiles

FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    cmake \
    build-essential \
    zlib1g-dev \
    libcgal-dev

COPY . /app
WORKDIR /app/cgal/

RUN cmake -DCMAKE_BUILD_TYPE=Release .
RUN make

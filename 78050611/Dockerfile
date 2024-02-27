FROM ubuntu:latest

RUN apt-get update -qq && apt-get install -y -qq cmake g++

COPY . .

RUN cmake -S . -B build
# RUN cmake --build build -j$(nproc)

RUN make -j$(nproc) -C build
RUN make -j$(nproc) DESTDIR=./dist -C build install

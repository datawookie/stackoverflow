FROM ubuntu:latest

RUN apt-get update -qq && apt-get install -y -qq cmake g++

COPY . .

RUN cmake -S . -B build
RUN cmake --build build -j$(nproc)

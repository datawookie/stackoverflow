FROM python:3.12.0

RUN apt-get update -qq && \
    apt-get install -y -qq cmake gfortran

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

RUN rm -rf build && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make

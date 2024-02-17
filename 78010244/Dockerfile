FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

ENV SPARK_HOME /opt/spark
ENV PATH="${SPARK_HOME}/bin:${PATH}"
ENV PATH="${SPARK_HOME}/python:${PATH}"
ENV PYSPARK_PYTHON python3
ENV JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64/jre"

RUN apt-get update -q && apt-get install -y -qq wget

RUN wget -q https://dlcdn.apache.org/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz && \
    tar zxvf spark-3.5.0-bin-hadoop3.tgz && \
    mv spark-3.5.0-bin-hadoop3 $SPARK_HOME && \
    rm spark-3.5.0-bin-hadoop3.tgz
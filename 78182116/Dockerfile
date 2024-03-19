FROM ubuntu:latest
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y openjdk-8-jdk dub wget rsync

RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo

RUN wget https://downloads.apache.org/kafka/3.7.0/kafka_2.13-3.7.0.tgz && \
    tar -xvf kafka_2.13-3.7.0.tgz && \
    mkdir -p /home/servidor-kafka/kafka && \
    rsync -av --remove-source-files kafka_2.13-3.7.0/ /home/servidor-kafka/kafka/ && \
    rm kafka_2.13-3.7.0.tgz

RUN wget https://downloads.apache.org/zookeeper/zookeeper-3.7.2/apache-zookeeper-3.7.2-bin.tar.gz && \
    tar -xvf apache-zookeeper-3.7.2-bin.tar.gz && \
    mkdir -p /home/servidor-kafka/zookeeper && \
    rsync -av --remove-source-files apache-zookeeper-3.7.2-bin/ /home/servidor-kafka/zookeeper/ && \
    rm apache-zookeeper-3.7.2-bin.tar.gz

WORKDIR /home/servidor-kafka/kafka

EXPOSE 9092 2181
USER docker

CMD ["/bin/bash"]

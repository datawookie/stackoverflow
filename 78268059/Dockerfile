FROM ubuntu:22.04

RUN useradd -m jenkins && \
    echo "umask 0002" >>/home/jenkins/.bashrc

USER jenkins
WORKDIR /home/jenkins

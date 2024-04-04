FROM ubuntu:22.04

ARG USER=jenkins
RUN useradd ${USER}

RUN echo "umask 007" >>/etc/profile
RUN echo "umask 007" >>/etc/bash.bashrc

USER ${USER}
WORKDIR /home/${USER}

CMD whoami && umask

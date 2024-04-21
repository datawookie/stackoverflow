FROM centos:7

ARG PYTHON_VERSION=3.10.14

RUN yum -y update && \
    yum groupinstall -y "Development Tools" && \
    yum install -y \
        gcc \
        make \
        openssl-devel \
        bzip2-devel \
        libffi-devel \
        zlib-devel \
        wget \
        libuuid-devel \
        libsqlite3x-devel \
        readline-devel \
        tk-devel \
        gdbm-devel \
        db4-devel \
        libpcap-devel \
        xz-devel

WORKDIR /usr/src
RUN wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz && \
    tar -zxf Python-${PYTHON_VERSION}.tgz

WORKDIR /usr/src/Python-${PYTHON_VERSION}
RUN ./configure --enable-optimizations --enable-shared --with-ensurepip=install && \
    make altinstall

RUN yum clean all && \
    rm -rf /var/cache/yum && \
    rm -rf /usr/src/Python-${PYTHON_VERSION}.tgz

RUN ln -sf /usr/local/bin/python3.10 /usr/bin/python3 && \
    ln -sf /usr/local/bin/pip3.10 /usr/bin/pip3

ENV LD_LIBRARY_PATH /usr/local/lib:$LD_LIBRARY_PATH

FROM rstudio/r-base:devel-centos7 AS base

WORKDIR /R_setup

COPY CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo

RUN wget -q https://download2.rstudio.org/server/centos7/x86_64/rstudio-server-rhel-2023.12.1-402-x86_64.rpm

RUN sed -i 's/enabled=1/enabled=0/' /etc/yum/pluginconf.d/fastestmirror.conf && \
    yum clean all && \
    yum makecache fast && \
    yum update && \
    yum install -y rstudio-server-rhel-2023.12.1-402-x86_64.rpm

CMD ["bash"]

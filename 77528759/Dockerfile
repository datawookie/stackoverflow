FROM centos:7

RUN yum install -y epel-release && \
    yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

ENV PERL_MM_USE_DEFAULT=1

RUN yum install -y \
        gcc \
        perl-App-cpanminus-1.6922-2.el7.noarch \
        perl-Class-MethodMaker-2.20-1.el7.x86_64 \
        perl-ExtUtils-MakeMaker-6.68-3.el7.noarch \
        openssl-1.0.2k-26.el7_9.x86_64

RUN cpanm \
        Fatal@2.37 \
        FFI::CheckLib@0.31 \
        Alien::Build::Plugin::Download::GitLab@0.01 \
        XML::SAX@1.02 \
        XML::LibXML@2.0210

RUN yum remove -y perl-App-cpanminus-1.6922-2.el7.noarch && \
    yum clean all

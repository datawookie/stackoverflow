FROM rocker/rstudio:4.3.1

ENV CRAN_REPO="https://packagemanager.posit.co/cran/__linux__/jammy/2024-02-01/"
ENV BIOC_REPO="https://ftp.gwdg.de/pub/misc/bioconductor/"
ENV BIOC_VERSION="3.18"

ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib/R/lib

RUN apt-get update && \
    apt-get install -y libxml2-dev

COPY ./install_scripts/setup_r.sh /install_scripts/setup_r.sh
RUN echo $LD_LIBRARY_PATH
RUN chmod u+x /install_scripts/setup_r.sh && \
    /install_scripts/setup_r.sh

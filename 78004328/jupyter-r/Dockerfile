FROM quay.io/jupyter/r-notebook

USER root

RUN apt-get update
RUN apt-get install -y --fix-missing \
    libssl-dev \
    libcurl4-openssl-dev \
    libxml2-dev \
    glpk-utils \
    libfontconfig1-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    libproj-dev \
    libglpk-dev \
    libfreetype6-dev \
    libpng-dev \
    libtiff5-dev \
    libjpeg-dev \
    mono-mcs \
    mono-xbuild \
    mono-runtime \
    libmono-system-data4.0-cil \
    r-cran-igraph

ENV R_LIBS_USER=/usr/lib/R/site-library/

RUN R -e 'install.packages("BiocManager", repos = "https://cloud.r-project.org")'
RUN R -e 'BiocManager::install(c("clusterProfiler", "AnnotationDbi", "org.Hs.eg.db"), ask=FALSE)'

EXPOSE 8888

RUN mkdir -p /etc/jupyter

RUN echo "c.NotebookApp.notebook_dir = '/app/notebooks'" >> /etc/jupyter/jupyter_lab_config.py
RUN echo "c.MappingKernelManager.kernel_cmd_timeout = 3600" >> /home/jovyan/.jupyter/jupyter_notebook_config.py
# Disable authentication.
RUN echo "c.NotebookApp.token = ''" >> /etc/jupyter/jupyter_lab_config.py

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

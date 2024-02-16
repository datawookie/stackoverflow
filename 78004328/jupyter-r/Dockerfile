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
        libfreetype6-dev \
        libpng-dev \
        libtiff5-dev \
        libjpeg-dev \
        mono-mcs \
        mono-xbuild \
        mono-runtime \
        libmono-system-data4.0-cil && \
    conda install -y -c conda-forge glpk gmp && \
    ln -s /opt/conda/include/libxml2/libxml /opt/conda/include/

RUN echo 'options(repos = c(CRAN = "https://cloud.r-project.org"))' >>/opt/conda/lib/R/etc/Rprofile.site

RUN R -e 'install.packages(c("BiocManager", "igraph"))'
RUN R -e 'BiocManager::install(c("clusterProfiler", "AnnotationDbi", "org.Hs.eg.db"), ask=FALSE, update=TRUE)'

EXPOSE 8888

RUN mkdir -p /etc/jupyter

RUN echo "c.NotebookApp.notebook_dir = '/app/notebooks'" >> /etc/jupyter/jupyter_lab_config.py
RUN echo "c.MappingKernelManager.kernel_cmd_timeout = 3600" >> /home/jovyan/.jupyter/jupyter_notebook_config.py

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

# Use the jupyter/r-notebook image as the base
FROM quay.io/jupyter/r-notebook

# Set the working directory to /app
WORKDIR /app

# Switch to the root user
USER root

# Install system dependencies
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
    r-cran-igraph \
    mono-mcs \
    mono-xbuild \
    mono-runtime \
    libmono-system-data4.0-cil

# Install R packages
RUN mamba install --yes \
    'r-BiocManager'\

# Install BiocManager packages
RUN R -e "BiocManager::install(c(\
    'clusterProfiler',\
    'AnnotationDbi',\
    'org.Hs.eg.db'\
))"

# Expose the Jupyter Notebook port
EXPOSE 8888

# Create JupyterLab configuration directory
RUN mkdir -p /etc/jupyter

# Add JupyterLab configuration to save notebooks in /app/notebooks
RUN echo "c.NotebookApp.notebook_dir = '/app/notebooks'" >> /etc/jupyter/jupyter_lab_config.py
RUN echo "c.MappingKernelManager.kernel_cmd_timeout = 3600" >> /home/jovyan/.jupyter/jupyter_notebook_config.py

# Command to run Jupyter Notebook
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

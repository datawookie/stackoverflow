FROM rockylinux:8.9

RUN dnf install -y epel-release
RUN dnf config-manager --set-enabled powertools
RUN dnf install -y R gsl-devel

RUN R -e 'install.packages("BiocManager", repos="https://cloud.r-project.org")'
RUN R -e 'BiocManager::install("DirichletMultinomial", ask = FALSE)'
RUN R -e 'library(DirichletMultinomial)'

#!/bin/bash

set -e
set -x
set -u

NCPUS=${NCPUS:--1}

cat <<END >$R_HOME/etc/Rprofile.site
options(
    repos = c(CRAN = '${CRAN_REPO}'),
    BioC_mirror = '${BIOC_REPO}',
    download.file.method = 'libcurl'
)
END

/usr/local/lib/R/site-library/littler/examples/update.r --ncpus ${NCPUS:--1}

install2.r --deps "NA" --error --skipinstalled --ncpus ${NCPUS:--1} \
    BiocManager \
    rstudioapi \
    remotes \
    languageserver \
    aws.s3 \
    usethis

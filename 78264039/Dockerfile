FROM rocker/tidyverse:4.3.2

RUN Rscript -e 'tinytex::install_tinytex()'

ENV PATH="${PATH}:/root/.TinyTeX/bin/x86_64-linux/"

RUN tlmgr install \
        multirow \
        colortbl \
        wrapfig \
        pdflscape \
        varwidth \
        threeparttable \
        ulem \
        anyfontsize \
        fancyhdr

COPY dummy.Rmd .
CMD R -e "rmarkdown::render('dummy.Rmd')"

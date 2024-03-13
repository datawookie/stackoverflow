FROM node:18-bookworm-slim as base

# ------------------------------------------------

FROM base as api_build

# ------------------------------------------------

FROM base as web_build

ARG ENV1=val1

# ------------------------------------------------

FROM node:18-bookworm-slim as serve

ARG ENV1=val1
ENV ENV1=${ENV1}

CMD echo $ENV1

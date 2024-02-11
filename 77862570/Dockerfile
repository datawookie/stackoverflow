FROM rasa/rasa-sdk:3.6.2

USER root

RUN apt-get update && \
    pip install --no-cache-dir requests

COPY ./actions /app/actions

USER 1001

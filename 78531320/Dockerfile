FROM ubuntu

RUN apt update -y && \
    apt install -y \
        git

WORKDIR /app

# Get around ownership issues.
RUN git config --global --add safe.directory /app

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD ["bash"]

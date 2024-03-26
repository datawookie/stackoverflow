FROM eclipse-temurin:17-jre-alpine

WORKDIR /app/kafka

RUN wget https://archive.apache.org/dist/kafka/3.5.1/kafka-3.5.1-src.tgz && \
    tar -zxvf kafka-3.5.1-src.tgz && \
    mv kafka-3.5.1-src/* . && \
    rm -rf kafka-3.5.1-src

CMD ls -lisa bin | grep kafka-s

ENTRYPOINT ["/bin/sh", "-c", "/__cacert_entrypoint.sh && top -b"]

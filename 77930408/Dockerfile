FROM ubuntu:22.04

RUN apt update -q && apt install -q -y redis-tools iputils-ping

COPY worker.sh .

CMD ["bash", "worker.sh"]

FROM ubuntu:22.04

WORKDIR /Lab3

RUN apt-get update -qq && \
    apt-get install -y -qq g++ valgrind

# Copy files AFTER pacman install, otherwise cached install not used.
#
COPY . .

RUN chmod +x testscr.sh

CMD ["./testscr.sh"]

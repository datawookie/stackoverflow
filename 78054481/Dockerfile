FROM debian:bookworm-20230919 as builder

RUN rm -f /etc/apt/apt.conf.d/docker-clean && \
    apt update && apt -y --no-install-recommends install build-essential

FROM debian:bookworm-20230919 as production

COPY --from=builder /var/cache/apt/ /var/cache/apt/
COPY --from=builder /var/lib/apt/lists/ /var/lib/apt/lists/

RUN apt -y --no-install-recommends install vim

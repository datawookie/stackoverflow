FROM alpine:latest

COPY file* /run/secrets/users/

COPY entrypoint.sh .

ENTRYPOINT ["sh", "entrypoint.sh"]

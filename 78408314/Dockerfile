FROM alpine:3.19

WORKDIR /app

COPY start.sh ./start.sh

RUN chmod +x start.sh

CMD [ "/app/main" ]
ENTRYPOINT [ "/app/start.sh" ]

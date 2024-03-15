FROM golang:1.22.1-alpine

WORKDIR /app

COPY cmd/ .

RUN go mod download

RUN go build -o main .

CMD ["/app/main"]

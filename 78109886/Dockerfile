FROM golang:alpine3.19

RUN apk add --no-cache curl

WORKDIR /app

COPY . .

RUN go mod tidy

RUN go build -o main .

RUN curl -o wait-for.sh https://raw.githubusercontent.com/eficode/wait-for/master/wait-for && \
    chmod +x wait-for.sh

CMD ["./wait-for.sh", "mysql:3306", "--", "./main"]

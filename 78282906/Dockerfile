FROM golang:alpine3.19

RUN apk add --no-cache curl

WORKDIR /app

COPY . .

RUN go mod tidy
RUN go build -o main .

CMD ./main

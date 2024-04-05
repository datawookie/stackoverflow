FROM golang:1.21 as build

WORKDIR /app

RUN apt-get update
RUN apt-get install -y libvips libvips-dev

COPY go.mod go.sum main.go .

RUN GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build \
        -tags netgo \
        -ldflags '-w -extldflags "-static"' \
        -o main main.go

FROM alpine:3.19


RUN apk add --no-cache ca-certificates

COPY --from=build /app/main /main

ENTRYPOINT [ "/main" ]

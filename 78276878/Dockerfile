FROM golang:1.21 as build

WORKDIR /app

RUN apt-get update
RUN apt-get install -y libvips-dev

COPY go.mod go.sum main.go .

RUN go mod download
RUN GOOS=linux GOARCH=amd64 CGO_ENABLED=1 go build \
        -tags netgo \
        -o main main.go

FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y libvips

COPY --from=build /app /app

ENTRYPOINT ["/app/main"]

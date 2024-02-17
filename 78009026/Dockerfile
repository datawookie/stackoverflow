FROM golang:alpine3.17 as builder

RUN apk add --no-cache $(apk search --no-cache | grep -q ^upx && echo -n upx) git \
  && git clone --depth=1 https://github.com/akamai/cli-purge \
  && cd cli-purge \
  && go mod tidy \
  && go build -o /akamai-purge -ldflags="-s -w" \
  && upx -3 -o/akamai-purge.upx /akamai-purge

RUN apk add --no-cache $(apk search --no-cache | grep -q ^upx && echo -n upx) git \
  && git clone --depth=1 https://github.com/akamai/cli \
  && cd cli \
  && go mod tidy \
  && go build -o /akamai -ldflags="-s -w" cli/main.go \
  && upx -3 -o/akamai.upx /akamai

FROM ubuntu:20.04

ENV AKAMAI_CLI_HOME=/cli

RUN mkdir -p \
        $AKAMAI_CLI_HOME/.akamai-cli/src/cli-purge/bin \
        $AKAMAI_CLI_HOME/.akamai-cli/logs

COPY --from=builder /akamai-purge.upx $AKAMAI_CLI_HOME/.akamai-cli/src/cli-purge/bin/akamai-purge
COPY --from=builder /go/cli-purge/cli.json $AKAMAI_CLI_HOME/.akamai-cli/src/cli-purge/cli.json

COPY --from=builder /akamai.upx /bin/akamai

COPY config $AKAMAI_CLI_HOME/.akamai-cli/config

RUN chmod -R a+rwx ${AKAMAI_CLI_HOME}

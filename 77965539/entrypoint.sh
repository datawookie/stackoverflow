#!/bin/sh

export YARN_VERSION=$(yarn -v)
exec "$@"
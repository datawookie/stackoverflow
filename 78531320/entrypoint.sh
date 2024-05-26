#!/bin/bash

export VERSION=$(git describe)

exec "$@"

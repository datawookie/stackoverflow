#!/bin/bash

npm ci

npm install playwright --with-deps

npm run env:dev

#!/usr/bin/env bash

docker build --platform linux/x86_64 -t selenium_automation_tests .
docker run --platform linux/x86_64 -p 4442-4444:4442-4444  -it selenium_automation_tests

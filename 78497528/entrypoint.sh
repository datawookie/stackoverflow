#!/bin/sh

cd /run/secrets/users
ls -l

for username in *; do
      echo "username is «$username»"
done

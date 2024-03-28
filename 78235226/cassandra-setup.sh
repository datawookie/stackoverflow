#!/bin/bash

echo "🔵 Starting setup."

until cqlsh -e "describe cluster" db_cassandra 9042 >/dev/null 2>&1; do
  echo "🟠 Waiting for Cassandra to be ready."
  sleep 10
done

echo "🟣 Cassandra is ready. Describe the keyspaces."
cqlsh -e "describe keyspaces" db_cassandra 9042

echo "🟢 Done!"

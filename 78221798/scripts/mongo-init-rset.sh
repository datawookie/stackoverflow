#!/bin/bash

# NOTE: this script does not force Auth on Mongo, but will allow root and other users to authenticate.
# WARNING: unauthenticated users can still log in.

start_mongo() {
    mongod --replSet rs0 --bind_ip_all
}

activate_rs() {
    echo "Waiting for Mongo to start..."
    sleep 5
    echo "INITIATE REPLICA SET"
    mongosh --host mongo --eval "rs.initiate()"
    echo "MAKE ADMIN USER FOR REPLICA SET"
    mongosh --host mongo --eval "db.createUser({ user: \"root\", pwd: \"root\", roles: [ { role: \"root\", db: \"admin\" } ] });" admin
}

activate_rs &
start_mongo

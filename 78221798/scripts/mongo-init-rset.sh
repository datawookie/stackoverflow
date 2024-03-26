#!/bin/bash

activate_rs() {
    echo "Waiting for Mongo to start..."
    sleep 5
    echo "INITIATE REPLICA SET"
    mongosh --host mongodb --eval "rs.initiate()"
    echo "MAKE ADMIN USER FOR REPLICA SET"
    mongosh --host mongodb --eval "db.createUser({ user: \"root\", pwd: \"root\", roles: [ { role: \"root\", db: \"admin\" } ] });" admin
}

activate_rs &

mongod --replSet rs0 --bind_ip_all
#!/bin/bash

initialise() {
    sleep 5
    mongosh --host mongodb --eval "rs.initiate()"
}

initialise &

mongod --replSet rs0 --bind_ip_all

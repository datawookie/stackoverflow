#!/bin/bash

echo "Worker starting... done!"

echo "Redis at $REDIS_HOST:$REDIS_PORT."

ping -c 5 $REDIS_HOST

echo "Sending PING to Redis..."

redis-cli -h $REDIS_HOST -p $REDIS_PORT -a $REDIS_PASSWORD PING

echo "Done!"

echo "Worker stopping... done!"

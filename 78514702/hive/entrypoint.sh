#!/bin/bash

POSTGRES_HOST=postgres

export PGPASSWORD='hivepassword'

psql -h $POSTGRES_HOST -U hiveuser hive  -c "\dt"


# # Set HADOOP_HOME
# export HADOOP_HOME=/opt/hadoop
# export PATH=$HADOOP_HOME/bin:$PATH

# # Copy hive-site.xml to Hive conf directory
# cp $HIVE_HOME/conf/hive-site.xml $HIVE_HOME/conf/

# # Start Hive Metastore
# nohup hive --service metastore &

# # Start HiveServer2
# hive --service hiveserver2

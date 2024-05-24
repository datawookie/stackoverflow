#!/bin/bash

rm /opt/hadoop/share/hadoop/common/lib/slf4j-reload4j-1.7.36.jar

if [ ! -f $HADOOP_CONF_DIR/log4j.properties ]; then
  cp $HADOOP_HOME/conf/log4j.properties $HADOOP_CONF_DIR/log4j.properties
fi

if [ ! -f $HIVE_HOME/conf/log4j.properties ]; then
  cp $HIVE_HOME/conf/log4j-hive.properties $HIVE_HOME/conf/log4j.properties
fi

export PGPASSWORD=$POSTGRES_PASSWORD
TABLE_EXISTS=$(psql -h postgres -U $POSTGRES_USER -d $POSTGRES_DB -tc "SELECT 1 FROM pg_tables WHERE schemaname='public' AND tablename='BUCKETING_COLS';")

if [ -z "$TABLE_EXISTS" ]; then
  echo "Initializing Hive schema"
  $HIVE_HOME/bin/schematool -initSchema -dbType postgres 2>&1 | grep -v '^$'
else
  echo "Hive schema is already initialized, skipping schema initialization"
fi

pid=$(pgrep -f 'hive.*service.*hiveserver2')
if [ -n "$pid" ]; then
  echo "Stopping running HiveServer2 process..."
  kill -9 $pid
fi

$HIVE_HOME/bin/hive --service metastore &

$HIVE_HOME/bin/hive --service hiveserver2

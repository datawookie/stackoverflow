#!/bin/bash

for f in /import/*.json
do
    name=$(basename $f | cut -d'.' -f1)
    mongoimport --db=APPDB --collection=$name --jsonArray --file=$f
done

#!/bin/bash

SAVEPATH=$HOME/Documents/save_path.txt

savepath () {
    pwd > $SAVEPATH
}

gotopath () {
    cd `cat $SAVEPATH`
}

#!/bin/bash

MY_PYTHONPATH="$PWD"
OLD_PYTHON_PATH="$PYTHONPATH"

START="start"
STOP="stop"
ARG=$1

start() {
    echo "$MY_PYTHONPATH"
    export PYTHONPATH="$MY_PYTHONPATH"
}

stop() {
    unset PYTHONPATH
    export PYTHONPATH="$OLD_PYTHON_PATH"
}

if [[ "$ARG" == "$START" ]]; then
    echo "start"
    start
elif [[ "$ARG" == "$STOP" ]]; then
    echo "stop"
    stop
else
    echo "Use start/stop"
fi
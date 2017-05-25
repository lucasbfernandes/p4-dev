#!/usr/bin/env bash

THIS_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

source $THIS_DIR/../../tools/defaults.sh

THIS_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

$CLI_PATH $THIS_DIR/build/simple_counter.json < $THIS_DIR/commands.txt

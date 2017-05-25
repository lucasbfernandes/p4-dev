#!/usr/bin/env bash

THIS_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

source $THIS_DIR/../../tools/defaults.sh

THIS_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

sudo python \
	$MININET_DIR/simple_counter/simple_counter.py \
	--behavioral-exe $SWITCH_PATH \
	--json $THIS_DIR/build/simple_counter.json
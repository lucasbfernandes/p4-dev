#!/usr/bin/env bash

THIS_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

source $THIS_DIR/../../tools/defaults.sh

$P4C_BM_SCRIPT p4/simple_counter.p4 --json build/simple_counter.json
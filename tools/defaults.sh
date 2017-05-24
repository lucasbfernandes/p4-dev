#!/usr/bin/env bash

set -e

THIS_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
BMV2_DIR="$THIS_DIR/../git_modules/bmv2"
P4C_BM_DIR="$THIS_DIR/../git_modules/p4c-bm"
FLOODLIGHT_DIR="$THIS_DIR/../git_modules/floodlight"

P4C_BM_SCRIPT="$P4C_BM_DIR/p4c_bm/__main__.py"
SWITCH_PATH="$BMV2_DIR/targets/simple_switch/simple_switch"
CLI_PATH="$BMV2_DIR/targets/simple_switch/sswitch_CLI"
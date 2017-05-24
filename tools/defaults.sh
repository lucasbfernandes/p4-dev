#!/usr/bin/env bash

set -e

THIS_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
BMV2_DIR="$THIS_DIR/../git_modules/bmv2"
P4C_BM_DIR="$THIS_DIR/../git_modules/p4c-bm"
FLOODLIGHT_DIR="$THIS_DIR/../git_modules/floodlight"
#!/usr/bin/env bash

set -e

sudo apt-get install -y \
	build-essential \
	ant \
	maven \
	python-dev

THIS_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
BMV2_DIR="git_modules/bmv2"
P4C_BM_DIR="git_modules/p4c-bm"
FLOODLIGHT_DIR="git_modules/floodlight"

cd $BMV2_DIR
bash install_deps.sh
bash autogen.sh
bash configure
make
sudo make install
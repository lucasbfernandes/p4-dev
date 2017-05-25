#!/usr/bin/env bash

set -e

sudo apt-get install -y \
	build-essential \
	ant \
	maven \
	python-dev

THIS_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
BMV2_DIR="$THIS_DIR/../git_modules/bmv2"
P4C_BM_DIR="$THIS_DIR/../git_modules/p4c-bm"
FLOODLIGHT_DIR="$THIS_DIR/../git_modules/floodlight"

cd $BMV2_DIR
bash install_deps.sh
bash autogen.sh
bash configure
make
sudo make install
cd $THIS_DIR

cd $P4C_BM_DIR
sudo pip install -r requirements.txt
sudo python setup.py install
cd $THIS_DIR

cd $FLOODLIGHT_DIR
git submodule init
git submodule update
ant
sudo mkdir /var/lib/floodlight
sudo chmod 777 /var/lib/floodlight
cd $THIS_DIR
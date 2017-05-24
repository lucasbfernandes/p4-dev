#!/usr/bin/env bash

set -e

TARGET_NAME=$1
TARGETS_DIR="targets"
P4_DIR="p4"
BUILD_SCRIPT="build.sh"
RUN_SCRIPT="run.sh"

echo "Creating directory..."
cd $TARGETS_DIR
mkdir $TARGET_NAME
echo "Done."

echo "Creating files..."
cd $TARGET_NAME
mkdir $P4_DIR
touch $BUILD_SCRIPT
chmod +x $BUILD_SCRIPT
touch $RUN_SCRIPT
chmod +x $RUN_SCRIPT
echo "Done."

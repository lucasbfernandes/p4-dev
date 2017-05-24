#!/usr/bin/env bash

set -e

THIS_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
TARGET_NAME=$1
TARGETS_DIR="$THIS_DIR/../targets"
MININET_DIR="$THIS_DIR/../mininet"
MININET_SCRIPT="$TARGET_NAME.py"
P4_DIR="p4"
BUILD_DIR="build"
BUILD_SCRIPT="build.sh"
RUN_SCRIPT="run.sh"
COMMANDS="commands.txt"

echo "Creating targets directory and files..."
cd $TARGETS_DIR
mkdir $TARGET_NAME
cd $TARGET_NAME
mkdir $P4_DIR
mkdir $BUILD_DIR
touch $BUILD_SCRIPT
chmod +x $BUILD_SCRIPT
touch $RUN_SCRIPT
chmod +x $RUN_SCRIPT
touch $COMMANDS
cd $THIS_DIR
echo "Done."

echo "Creating mininet directory and files..."
cd $MININET_DIR
mkdir $TARGET_NAME
cd $TARGET_NAME
touch $MININET_SCRIPT
cd $THIS_DIR
echo "Done."
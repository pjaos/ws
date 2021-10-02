#!/bin/sh

# This is used for testing the tool on a RPi.

# A single argument is required that is the target address.
HOST=$1
#The folder to scp the installer files into.
TARGET_FOLDER=/home/pi/pip/ws

scp -r ws scripts install.sh uninstall.sh setup.py README.md pi@$HOST:$TARGET_FOLDER

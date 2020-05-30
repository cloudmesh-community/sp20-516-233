#!/bin/bash

# install the Mosquitto Broker
sudo apt-get install mosquitto

# install websocket dependencies
sudo apt-get update
sudo apt-get install build-essential python quilt python-setuptools python3
sudo apt-get install libssl-dev
sudo apt-get install cmake
sudo apt-get install libc-ares-dev
sudo apt-get install uuid-dev
sudo apt-get install daemon
sudo apt-get install libwebsockets-dev

# get wesocket support for the Mosquitto Broker
wget http://mosquitto.org/files/source/mosquitto-1.6.9.tar.gz
tar zxvf mosquitto-1.6.9.tar.gz
cd mosquitto-1.6.9/
sudo vim config.mk


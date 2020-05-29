#!/bin/bash

# build Mosquitto configuration with websockets
make
sudo make install
sudo cp mosquitto.conf /etc/mosquitto


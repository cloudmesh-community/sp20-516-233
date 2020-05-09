# Code Setup sp20-516-233 Holly Zhang

## Installing Mosquitto Broker

The Mosquitto Broker needs to be installed so that MQTT services can be run on 
the localhost. Use the following command to install the Mosquitto Broker:

```bash
$ sudo apt-get install mosquitto
```

## Installing the Paho MQTT Library

To install the the Paho MQTT library, use the following command:

```bash
$ pip install paho-mqtt
``` 

## Change the Localhost IP in Scripts

The localhost IP will need to be found on the device running the MQTT service. 
To get the IP address, use the following command:

```bash
$ hostname -I
``` 
After getting the localhost IP, navigate to `publisher.py` and `subscriber.py`. 
Both scripts should have a variable called `broker_ip`. Change the string value 
of `broker_ip` to the localhost IP in string form.

## Change the Directory Path

In `subscriber.py`, make sure to change the path saved in `dir_location` so that 
the files will be written in the correct location.

## How to Run the Script

First, open two terminal windows. Run `subscriber.py` first in one terminal 
window and then run `publisher.py` in another window.



  
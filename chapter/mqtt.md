# MQTT sp20-516-233 Holly Zhang

## Paho Python Client

### Supported Features

> * MQTT 3.1
> * MQTT 3.1.1
> * LWT
> * SSL/TLS
> * Automatic Reconnect
> * Offline Buffering
> * WebSocket Support
> * Standard TCP Support
> * Non-Blocking API

### Unsupported Features

> * MQTT 5.0
> * Message Persistence
> * High Availability

### Installation

The following two sections show how to download the Paho Python Client provided 
by [@eclipse-paho]. Choose only one of them.

#### Python Pip Download
Make sure that pip had been downloaded and updated before entering the following 
command:
```bash
$ pip install paho-mqtt
```

#### GitHub Source Code Download

```bash
$ git clone https://github.com/eclipse/paho.mqtt.python
$ cd paho.mqtt.python
$ python setup.py install
```

## Mosquitto Python Client

The Mosquitto Python client is depreciated and is now part of the Eclipse Paho 
project [@eclipse-mosquitto]. The previous section shows how to use the Paho 
Python client.

## AMQP Python Client

This is not supported for Python 3.8 [@amqp].  

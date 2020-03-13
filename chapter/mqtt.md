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

#### Connecting a Client to a Public Server

This creates a client that connects to the `mqtt.eclipse.org` public server on 
`port 1883`. The parameter `keepalive=60` sets the maximum amount of seconds 
allowed for the broker and client to communicate with each other. 

```
client = mqtt.Client()

---------- client setup code in between -------------

client.connect("mqtt.eclipse.org", 1883, 60)
```

#### Connecting a Client to a Localhost

```
client = mqtt.Client("mqttClient", clean_session=False, protocol=mqtt.MQTTv31)

---------- client setup code in between -------------

client.connect(host="insert_localhost_ip_address", port=1883)
```

#### Subscribing

```
#qos = 0
qos = 1
#qos = 2
client.subscribe("subscriber_message", qos)
```

#### Publishing

```

```

#### Logging

```
def on_log():
    # include logging code
client.on_log = on_log
```

## Mosquitto Python Client

The Mosquitto Python client is depreciated and is now part of the Eclipse Paho 
project [@eclipse-mosquitto]. The previous section shows how to use the Paho 
Python client.
  

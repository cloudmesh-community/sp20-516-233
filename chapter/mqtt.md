# MQTT sp20-516-233 Holly Zhang

## Eclipse Paho-MQTT Python Client

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

### Connecting a Client to a Public Server

This creates a client that connects to the `mqtt.eclipse.org` public server on 
`port 1883`. The parameter `keepalive=60` sets the maximum amount of seconds 
allowed for the broker and client to communicate with each other. Other public 
servers can be used by replacing `mqtt.eclipse.org` with the desired server's 
url or its IP address.

```
client = mqtt.Client()

---------- client setup code in between -------------

client.connect("mqtt.eclipse.org", 1883, 60)
```

### Connecting a Client to a Localhost

MQTT services can be run on a localhost instead of a public server. In order to 
run it locally, an MQTT broker needs to be installed on the localhost. The 
following command shows how to install the Mosquitto Broker:

```bash
$ sudo apt-get install mosquitto
```

After installing the broker, the localhost IP needs to be found. This can be 
done using the following command:

```bash
$ hostname -I
```

Once the localhost IP is found, use it in the place of `localhost_ip`.

```
client = mqtt.Client("mqttClient", clean_session=False, protocol=mqtt.MQTTv31)

---------- client setup code in between -------------

client.connect(host="localhost_ip", port=1883)
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

## Mosquitto Python

The Mosquitto Python client is depreciated and is now part of the Eclipse Paho 
project [@eclipse-mosquitto]. The previous section shows how to use the Paho 
Python client.
  

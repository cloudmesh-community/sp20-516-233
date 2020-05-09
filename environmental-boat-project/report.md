# Environmental Robot Boat sp20-516-233 Holly Zhang

## Abstract

We introduce a network architecture using MQTT services to send sensor data from 
an environmental robot boat to various cloud AI services. 

## Evaluating Messaging Protocols

### MQTT

This messaging protocol was specifically made for devices with low capacities 
and requires low energy to execute [@rabbit]. Since a large amount of energy is 
consumed from the the boat's battery by the motors, we want the program to use 
as little energy as possible. Furthermore, the emphasis on low end devices 
means that it executing the code on a Raspberry Pi 3B+ should be possible with 
this protocol. 

### STOMP

STOMP is a protocol that utilizes text-based messaging [@rabbit]. Its 

### AMQP

This will most likely not be used in the project since the Python library for 
AMQP does not support Python 3.8 [@amqp]. Furthermore, it is mostly used in 
industrial settings.  

## Evaluating Messaging Toolkits

### MQTT Toolkits

#### Paho Python Client

Will most likely use this since MQTT uses low energy.
[@eclipse-paho]

#### Mosquitto Python Client

The Mosquitto Python library is now depreciated so it will not be used. Instead, 
it has been added into the Eclipse Paho project [@eclipse-mosquitto].

### STOMP Toolkits


### Other Toolkits

#### RabbitMQ

RabbitMQ supports multiple messaging protocols such as MQTT, STOMP, and a few 
versions of AMQP. However, it has AMQP 0-9-1 as its main messaging protocol, 
while other messaging protocols must be downloaded as plugins from the website 
[@rabbit]. The appropriate plugins can be found through the following link:

<https://www.rabbitmq.com/protocols.html>  

## Network Architecture

>* Server: mqtt.eclipse.org
>* Port: (default) 1883
>* Subscribe to messages: OpenAgBloom/#
>* The two messages are: OpenAgBloom/Air/BME, OpenAgBloom/GPS/Loc

### Client

The first line of code creates a MQTT client. The commented line connects the 
client to the public server named `mqtt.eclipse.org` on port 1883. 

```
client = mqtt.Client()

client.connect("mqtt.eclipse.org", 1883, 60)
```

This creates a MQTT client that runs on a local server on port 1883. The 
`client_id` specifies a name for the client. If `client_id` is left empty, then 
it will be automatically assigned a random name. We set `clean_session=False` 
because we want the broker to keep information about the subscriptions and 
queued messages whenever the client disconnects. We need to specify the MQQT 
`protocol` version since the automatic default can change with updates.  

```
client = mqtt.Client("mqttClient", clean_session=False, protocol=mqtt.MQTTv31)

---------- other code for client setup in between -------------

client.connect(host="insert_localhost_ip_address", port=1883)
```

#### How to Find the Local Host IP Address

On Linux and MacOS use the following command in terminal:

```bash
$ hostname -I
``` 

On Windows, use the following command on Command Prompt:

```bash
$ ipconfig
```

#### Subscriber

Here we have assign the subscriber message as `OpenAgBloom/#` with a quality of 
service `qos` of 1. We choose `qos=1` because we want to be sure that the 
messages are sent to the broker. However, it is possible that there are 
duplicate messages so additional code will be needed to prevent this. Another 
possibility is using `qos=2` which ensures that   

```
client.subscribe("subscriber_message", 1)
```

#### Publisher

```

```

#### Logging

To create a log, define a Python function called `on_log` that contains all the 
necessary logging information. Then set `client.on_log = on_log` to start 
logging the information. 

```
def on_log():
    # include logging code
client.on_log = on_log
```


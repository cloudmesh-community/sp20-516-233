# MQTT Project Proposal sp20-516-233 Holly Zhang

## Project Objective

This project attempts to create a network architecture using the MQTT protocol 
to send sensor data from a robot boat to subscribing clients. Users can choose 
whether subscribing clients save the data as a file or have the clients connect 
to a web browser to see the sensor data live in the case the client is unable to 
write files.     

## Project Plan

### Setting up MQTT

#### Paho Python Client & Paho Javascript Client

Clients that save the sensor as files will use the regular MQTT protocol. This 
will be written using the `Paho Python Client` which is called the `paho-mqtt` 
library on python. Clients that want to see the sensor data through a web 
browser will use the MQTT protocol over websockets. This will be written in 
Javascript using the the Paho Javascript Client.

#### Broker

So far, the broker in the MQTT protocol will be the Mosquitto Broker installed 
on a localhost. Mosquitto has the ability to use websockets, but it has to be 
manually configured by users. If the configuration of websockets on Mosquitto 
seems too time complicated, then another broker with MQTT and websocket 
capabilities will be selected instead. Another possible broker is RabbitMQ. 
RabbitMQ has a plugin that allow MQTT over websockets and is compatible with the 
Python Javascript Client.  

### Testing the MQTT Protocol

To check if the code works, one virtual machine will be assigned as the broker 
while other virtual machines will be assigned as subscribers, publishers, or 
both. The subscribers will run a python script that gets data from the broker, 
cleans the data, and then write it to a desired file location. The publishers on 
the other hand will be sending data to the broker. Since this is a simulation, 
the scripts for the publishers will generate random messages to the broker. For 
virtual machines that represent both subscribers and publishers, they will have 
a script that combines the first two scripts.

### Testing the MQTT Protocol over Websockets

For this, a user interface will need to be made so that the  

### Quality of Service




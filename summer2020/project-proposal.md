# MQTT Project Proposal sp20-516-233 Holly Zhang

## Project Objective

This project attempts to create a network architecture using the MQTT protocol 
to send sensor data from a robot boat to subscribing clients. Users can choose 
whether subscribing clients save the data as a file or have the clients connect 
to a web browser to see the sensor data live in the case the client is unable to 
write files.     

## Project Plan

### MQTT Tools

#### Paho Python Client & Paho Javascript Client

Clients that save the sensor as files will use the regular MQTT protocol. This 
will be written using the Paho Python Client which is called the paho-mqtt 
library on python. Clients that want to see the sensor data through a web 
browser will use the MQTT protocol over websockets. This will be written in 
Javascript using the the Paho Javascript Client.

#### Broker

So far, the broker in the MQTT protocol will be the Mosquitto Broker installed 
on a localhost. The Mosquitto Broker can use websockets, but it has to be 
manually configured by users. If the configuration of websockets on Mosquitto 
seems too time complicated, then another broker with MQTT and websocket 
capabilities will be selected instead. Another possible broker is RabbitMQ. 
RabbitMQ has a plugin that allow MQTT over websockets and is compatible with the 
Python Javascript Client.  

### Testing the MQTT Protocol

To check if the code works, one virtual machine will be assigned as the broker 
while other virtual machines will be assigned as subscribers, publishers, or 
both. All the virtual machines will be installed with the Paho Python Client and 
Paho Javascript Client so that they can use MQTT and MQTT over websockets. The 
virtual machine that is assigned as the broker will also download the selected 
broker for this project so it can run the MQTT service locally. The publishers 
on the other hand will be sending data to the broker. Since this is a 
simulation, the scripts for the publishers will generate random messages to the 
broker. The subscribers will run a python script that gets data from the broker, 
cleans the data, and then write it to a desired file location. For virtual 
machines that represent both subscribers and publishers, they will have a script 
that combines the first two scripts. 

### Testing the MQTT Protocol over Websockets

For this, a user interface will need to be made so that the client can connect  
to the broker through a web browser. The user will enter information such as the 
broker's IP address, port number, and possibly other information as well for a
more customized service. 

### MQTT Configuration

The data from the sensors should not be dropped. This means that the quality of 
service for the MQTT protocol should at least be 1. However, the data should 
also not have duplicates. This means that a qos of 2 may be wanted. The qos 
levels 1 and 2 will be tested to see which one is better. Although a qos of 2 
meets the requirement, it may be too slow for the data. If a qos of 2 is too 
slow, then a qos of 1 will be implemented. Since a qos of 1 may send duplicates, 
code will need to be developed to check for duplicates. 

The clients should also be configured to reconnect to the broker in case the 
connection is lost and send the data it had before disconnecting. This can be 
done by setting the client sessions to `False` so that previous messages before 
disconnection are retained and sent on reconnection. This can be tested by 
turning the broker on and off and seeing whether the subscribers still receive 
the messages.

It may be useful to keep track of messages and errors so a logger can be 
implemented. To include logging, a logging package needs such as python's PEP 
282 needs to be downloaded. 

If the sensor should only be accessed by certain users, a sign in option 
can also be included. The users with access will have their username and 
passwords set in the broker using a script.   




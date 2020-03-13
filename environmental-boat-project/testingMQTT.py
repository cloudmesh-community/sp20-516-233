import paho.mqtt.client as mqtt

#Server: mqtt.eclipse.org
#Port: (default) 1883
#Subscribe to messages: OpenAgBloom/#
#The two messages are: OpenAgBloom/Air/BME
#                      OpenAgBloom/GPS/Loc

#These are live data, pulled from a BME280 Bosch sensor (Temperature, Humidity, Barometer) and my GPS

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")
    # subscribe to qos=1
    #client.subscribe("OpenAgBloom/#, 1")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    m1 = "OpenAgBloom/Air/BME"
    m2 = "OpenAgBloom/GPS/Loc"

    if msg == m1:
        print(m1)
    if msg == m2:
        print(m2)

def on_log():
    # get time
    print("");

# MQTT broker on local host
#broker = "192.168.1.254"
client = mqtt.Client("mqttClient", clean_session=False, protocol=mqtt.MQTTv31)
client.on_connect = on_connect
client.on_message = on_message
client.on_log = on_log

client.connect(host="192.168.1.254", port=1883)

# right now it is being running publicly
#client.connect("mqtt.eclipse.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
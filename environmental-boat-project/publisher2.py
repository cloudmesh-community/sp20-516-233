import paho.mqtt.client as mqtt

# get the localhost IP by using "hostname -I" in terminal
broker_ip = "10.128.0.3"

# 1883 is a default port that is unencrypted
broker_port = 1883

def imitation_bme():
    bme_data = ""
    return bme_data

if __name__ == '__main__':
    client = mqtt.Client()
    client.connect(broker_ip, broker_port)
    client.publish(topic="OpenAgBloom/Air/BME", payload=imitation_bme(), qos=1,
                   retain=False)

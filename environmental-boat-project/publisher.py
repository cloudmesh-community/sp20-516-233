import paho.mqtt.client as mqtt

# get the localhost IP by using "hostname -I" in terminal
broker_ip = "192.168.1.254"

# 1883 is a default port that is unencrypted
broker_port = 1883

def imitation_gps():
    gps_data = ""
    return gps_data

if __name__ == '__main__':
    client = mqtt.Client()
    client.connect(broker_ip, broker_port)
    client.publish(topic="OpenAgBloom/GPS/Loc", payload=imitation_gps(), qos=1,
                   retain=False)
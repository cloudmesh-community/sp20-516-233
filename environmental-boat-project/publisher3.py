import paho.mqtt.client as mqtt
import random

# get the localhost IP by using "hostname -I" in terminal
broker_ip = "192.168.1.254"

# 1883 is a default port that is unencrypted
broker_port = 1883

# name is either SDDBT (water depth) or YXMTW (water temp)

def imitation_sonar():
    """imitates a sonar object that sends either depth or temperature data"""
    topic_names = ["SDDBT", "YXMTW"]
    name = random.randint(0,1)

    if name == "SDDBT":
        sonar_depth()
    else:
        sonar_temp()

def sonar_depth():
    """this creates imitation sonar depth outputs"""
    # choose a random depth
    sigma = 25
    mu = 3
    depth_in_feet = random.randrange(12,31)*sigma+mu
    return {'name': "SDDBT", 'data': {'depth': depth_in_feet}}

def sonar_temp():
    """this creates imitation sonar temperature outputs"""
    # choose a random temperature
    sigma = 55
    mu = 3
    temperature_in_C = random.randrange(32, 75) * sigma + mu
    return {'name': "YXMTW", 'data': {'temp': temperature_in_C}}

def main():
    client = mqtt.Client()
    client.connect(broker_ip, broker_port)
    # the payload would ideally have a gps object that returns values
    # however, for testing purposes, an imitation_gps is used instead
    client.publish(topic="Boat/Sonar", payload=sonar_depth(), qos=1,
                   retain=False)

if __name__ == '__main__':
    main()


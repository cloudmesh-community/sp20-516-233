import paho.mqtt.client as mqtt
import random

# get the localhost IP by using "hostname -I" in terminal
broker_ip = "10.128.0.3"

# 1883 is a default port that is unencrypted
broker_port = 1883

# name is either SDDBT (water depth) or YXMTW (water temp)

def imitation_sonar():
    """imitates a sonar object that sends either depth or temperature data"""
    return  str(sonar_depth()) + "_"+ str(sonar_temp())


def sonar_depth():
    """this creates imitation sonar depth outputs"""
    # choose a random depth
    sigma = 25
    mu = 3
    depth_in_feet = random.randrange(12,31)*sigma+mu
    return depth_in_feet
#{'name': "SDDBT", 'data': {'depth': depth_in_feet}}

def sonar_temp():
    """this creates imitation sonar temperature outputs"""
    # choose a random temperature
    sigma = 55
    mu = 3
    temperature_in_C = random.randrange(32, 75) * sigma + mu
    return temperature_in_C
#{'name': "YXMTW", 'data': {'temp': temperature_in_C}}


def main():
    client = mqtt.Client()
    client.connect(broker_ip, broker_port)

    # the payload would ideally have a gps object that returns values
    # however, for testing purposes, an imitation_gps is used instead
    while True:
        sonar_data = imitation_sonar()
        client.publish(topic="Boat/Sonar", payload=sonar_data, qos=1,retain=False)

if __name__ == '__main__':
    main()


import paho.mqtt.client as mqtt
import random

# get the localhost IP by using "hostname -I" in terminal
broker_ip = "10.128.0.3"

# 1883 is a default port that is unencrypted
broker_port = 9001

# name is either SDDBT (water depth) or YXMTW (water temp)

def imitation_sonar():
    """imitates a sonar object that sends either depth or temperature data"""
    return  str(sonar_depth()) + "_" + str(sonar_temp())

def sonar_depth():
    """this creates imitation sonar depth outputs"""
    # choose a random depth
    st_dev = 10
    mean = 20
    depth_in_feet = random.gauss(mean, st_dev)
    return depth_in_feet
#{'name': "SDDBT", 'data': {'depth': depth_in_feet}}

def sonar_temp():
    """this creates imitation sonar temperature outputs"""
    # choose a random temperature
    st_dev = 15
    mean = 50
    temperature_in_C = random.gauss(mean, st_dev)
    return temperature_in_C
#{'name': "YXMTW", 'data': {'temp': temperature_in_C}}


def main():
    client = mqtt.Client("web_client", transport='websockets')
    client.connect(broker_ip, broker_port)

    # the payload would ideally have a gps object that returns values
    # however, for testing purposes, an imitation_gps is used instead
    while True:
        sonar_data = imitation_sonar()
        client.publish(topic="Boat/Sonar", payload=sonar_data, qos=1,retain=False)

if __name__ == '__main__':
    main()
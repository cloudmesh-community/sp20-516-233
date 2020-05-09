import paho.mqtt.client as mqtt

# get the localhost IP by using "hostname -I" in terminal
broker_ip = "10.128.0.3"

# 1883 is a default port that is unencrypted
broker_port = 1883


def imitation_gps():
    """this creates imitation gps outputs"""

    gps_data = {'name': 'some_name', 'data': {'time':timestamp}, 'lat': LatDec,
              'lon':LonDec}
    return gps_data

if __name__ == '__main__':
    client = mqtt.Client()
    client.connect(broker_ip, broker_port)
    # the payload would ideally have a gps object that returns values
    # however, for testing purposes, an imitation_gps is used instead
    client.publish(topic="OpenAgBloom/GPS/Loc", payload=imitation_gps(), qos=1,
                   retain=False)

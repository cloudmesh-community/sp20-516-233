import paho.mqtt.client as mqtt
import csv
import os.path

# get the localhost IP by using "hostname -I" in terminal
broker_ip = "10.128.0.3"

# 1883 is a default port that is unencrypted
broker_port = 1883

# location where the sensor data will be written to
dir_location = "/home/sp20-516-233/environmental-boat-project/"
bme_filename = "bme.csv"
gps_filename = "gps.csv"
sonar_filename = "sonar.csv"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # subscribe to qos=1
    client.subscribe("OpenAgBloom/#", qos=1)
    client.subscribe("Boat/#", qos=1)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_message_from_gps(client, userdata, msg):
    print(msg.topic+"_"+str(msg.payload.decode()))

    # write gps data in file
    gps_info = msg.payload.decode()

    # check if the file exists
    file_exists = os.path.isfile(dir_location+gps_filename)

    # write the data into a file
    with open(gps_filename, "a") as file:
        headers = []
        file.write(gps_info)

def on_message_from_bme(client, userdata, msg):
    print(msg.topic+"_"+msg.payload.decode())
    # get the temp, humidity, and barometer info
    bme_info = msg.payload.decode()

    # write the data into a file
    with open(bme_filename, "a") as file:
        file.write(bme_info)

def on_message_from_sonar(client, userdata, msg):
    print(msg.topic+"_"+msg.payload)
    # get the temperature and depth
    sonar_info = msg.payload

    # check if the file exists
    file_exists = os.path.isfile(dir_location + sonar_filename)
    print(file_exists)

    # write the data into a file
    with open(sonar_filename, "r+") as file:
        headers = ["Id", "Depth", "Temperature_C"]

        # give an Id number for the data entry
        id_num = str(len(file.read().split("/n"))+1)

        writer = csv.DictWriter(file, delimiter=',', fieldnames=headers)
        if not file_exists:
            print("writing header")
            # write the header if the file did not exist earlier
            writer.writeheader()
        
        print("writing data")
        # extract the water depth and temperature
        sonar_info = sonar_info.split("_")
        file.writerow({"Id":id_num, "Depth":sonar_info[0], "Temperature_C":sonar_info[1]})

def on_log(date, hour, message):
    # get time
    print(message +"_"+ date +"_"+ hour);

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect

    # process messages
    client.on_message = on_message

    # connect to localhost broker
    client.connect(broker_ip, broker_port)

    # have callbacks on msg topics
    client.subscribe("OpenAgBloom/Air/BME", qos=1)
    client.subscribe("OpenAgBloom/GPS/Loc", qos=1)
    client.message_callback_add("OpenAgBloom/Air/BME", on_message_from_bme)
    client.message_callback_add("OpenAgBloom/GPS/Loc", on_message_from_gps)

    client.loop_forever()

    # need to figure out if the thing disconnected previously and see if there
    # are leftover messages
    # need to check for duplicates

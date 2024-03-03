import paho.mqtt.client as mqtt #import the client1
from random import randint
from time import sleep
import datetime
import serial

topics = [('system/plant/soilmoisture', 0), 
          ('system/pump/waterlevel', 0)]

soilmsgs = ['TIME', 'Plant']

pumpmsgs = ['ALERT', 'STARTING']

clientID = f"laptop{randint(0,100)}"
broker="test.mosquitto.org"
port = 1883

def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print(f"Connected to {broker}")

def connect() -> mqtt:
    print(f"Creating new instance as {clientID}")
    client = mqtt.Client(clientID)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client, topic, i, msg):
    result = client.publish(str(topic[i][0]), f"{msg}")
    status = result[0]
    if status == 0:
        print(f'Sent "{msg}" to {topic[i][0]}')

def main():
    client = connect()
    client.loop_start()
    seri = serial.Serial('/dev/ttyACM0', 115200, timeout=0)
    seri.reset_input_buffer()
    while True:
        #do message stuff
        # 1. write to a log file
        # 2. send the write to the laptop as well

        #make the pi tell the arduino to capture data
        data = seri.readline().decode().rstrip()

        if data != '':
             for i in soilmsgs:
                    if data[0:len(i)] == i:
                        print("This is a plant msg")
                        publish(client, topics, 0, data)
                    else:
                        print("This is not a plant msg")
                        publish(client, topics, 1, data)
             f = open("datalog.txt", "a")
            # now = datetime.now(tz = datetime.timezone.utc)
            # current_time = now.strftime("%H:%M:%S")
             f.write(" " + data + "\n")
             f.close()




if __name__ == '__main__':
    main()
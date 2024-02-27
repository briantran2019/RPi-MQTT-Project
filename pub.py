import paho.mqtt.client as mqtt #import the client1
import random
from include import interactive

topics = [('system/plant/soilmoisture', 0), 
          ('system/plant/numtimeswatered', 0),
          ('system/pump/waterlevel', 0)]
clientID = f"laptop{random.randint(0,100)}"
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

def main():
    client = connect()
    client.loop_start()
    while True:
        interactive(client, topics)

if __name__ == '__main__':
    main()
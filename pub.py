import paho.mqtt.client as mqtt #import the client1
import random


topics = [('system/plant/soilmoisture', 0), 
          ('system/plant/numtimeswatered', 0),
          ('system/pump/waterlevel', 0)]
clientID = f"laptop{random.randint(0,100)}"
broker="test.mosquitto.org"
port = 1883

def connect() -> mqtt:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print(f"Connected to {broker}")
    print("Creating new instance")
    client = mqtt.Client(clientID)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client, topic, i, j, msg):
    result = client.publish(str(topic[i][j]), f"{msg}")
    status = result[0]
    if status == 0:
        print(f"Send messsage to {topic[i][j]}")

def main():
    client = connect()
    client.loop_start()
    publish(client, topics, 0, 0, "Your mom")
    client.loop_stop() #stop the loop

if __name__ == '__main__':
    main()
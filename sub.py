import paho.mqtt.client as mqtt #import the client1
import random
from pub import publish

topics = [('system/plant/soilinfo', 0), 
          ('system/pump/waterinfo', 0)]
clientID = f"rpi{random.randint(0,100)}"
broker = "test.mosquitto.org"
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

def on_message(client, userdata, message):
    print("message received:" ,str(message.payload.decode("utf-8")))
   # print("message topic =",message.topic)

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed to Topics: ", end = "")
    for i in range(len(topics)):
        if i < len(topics) - 1:
            print(f'{topics[i][0]}, ', end = "")
        else:
            print(f'{topics[i][0]}')

def subscribe(client: mqtt):
    client.subscribe(topics)
    client.on_subscribe = on_subscribe
    client.on_message = on_message

def main():
    client = connect()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    main()
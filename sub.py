import paho.mqtt.client as mqtt #import the client1
import random

print("creating new instance")
client = mqtt.Client(f"rpi{random.randint(0,100)}") #create new instance

topics = [('system/plant/soilmoisture', 0),
          ('system/plant/numtimeswatered', 0),
          ('system/pump/waterlevel', 0)]

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
client.on_message=on_message #attach function to callback

print("connecting to broker")
broker_address="test.mosquitto.org"
client.connect(broker_address, 1883) #connect to broker
print("Subscribing to topic " + str(topics))
client.subscribe(topics)
client.loop_forever()
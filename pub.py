import paho.mqtt.client as mqtt #import the client1
from random import randint
from time import sleep
import hashlib

topics = [('system/plant/soilinfo', 0), 
          ('system/pump/waterinfo', 0)]

msgs = ['Current Moisture: ', 'Plant needs watering.', 'Attempting to water plant.', 'Plant does not need watering.', 'WATERING STATUS: SUCCESS']

clientID = f"laptop{randint(0,100)}"
broker = "broker.emqx.io"
port = 1883

def hash_password(input):
    return (hashlib.md5(input.encode()).hexdigest() == '051ebc83e3617c4304d6f5ba51d2cc75')

def login():
    user_input = input("Enter password: ")
    return hash_password(user_input)

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
    if login():
        client = connect()
        client.loop_start()
        
        while True:
            sleep(1)
            data = input("The message you would like to publish: ")
            if data != '':
                for i, msg in enumerate(msgs):
                    if data.startswith(msg):
                        publish(client, topics, 0, data)
                        break
                else:
                    publish(client, topics, 1, data)
                f = open("datalog.txt", "a")
                # now = datetime.now(tz = datetime.timezone.utc)
                # current_time = now.strftime("%H:%M:%S")
                f.write(" " + data + "\n")
                f.close()
    else:
        print('Wrong password')

if __name__ == '__main__':
    main()
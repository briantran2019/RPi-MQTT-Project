import time

def publish(client, topic, i, msg):
    result = client.publish(str(topic[i][0]), f"{msg}")
    status = result[0]
    if status == 0:
        print(f'Sent "{msg}" to {topic[i][0]}')

def getTopic() -> str:
    while True:
        topic = input("Which topic would you like to publish to?\n\
1. system/plant/soilmoisture\n\
2. system/plant/numtimeswatered\n\
3. system/pump/waterlevel\n")
        if topic not in ["1", "2", "3"]:
            print("Try again.\n")
        else:
            break
    return topic

def interactive(client, topics):
    time.sleep(1)
    message = input("What would you like to publish?\n")
    topic = getTopic()
    match topic:
        case '1':
            publish(client, topics, 0, message)
        case '2':
            publish(client, topics, 1, message)
        case '3': 
            publish(client, topics, 2, message)
        case _:
            print("Invalid choice\n")
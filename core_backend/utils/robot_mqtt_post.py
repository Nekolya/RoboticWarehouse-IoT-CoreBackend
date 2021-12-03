import paho.mqtt.client as mqtt
import asyncio
import json 
from os import environ


def publish():
    client = mqtt.Client()
    def on_publish(client,userdata,result):             #create function for callback
        print("data published \n")
        pass
    client.on_publish = on_publish
    client.connect('localhost', 1883, 60)
    client.publish("robots/tasks", "Hello robots!")
    print("published")
    
    
if __name__ ==  '__main__':
    publish()
import paho.mqtt.client as mqtt
import asyncio
import json 


class RobotsConnection():
    def __init__(self):
       self.client = mqtt.Client()


    async def publish(self):
        self.client.publish("robots/tasks", "Hello robots!")
        print("published")

    async def connect(self):
        def on_message(client, userdata, message):
        #   if message.payload.decode() == "Hello world!":
            data = json.loads(message.payload.decode("utf-8"))
            print("\nmessage from robot = ", data['model'], ', with id = ', data['id'], sep='')
            print("\nfull data =", data)
            print("\nmessage topic =",message.topic)
            print('\n____________\n')
            # print("message qos=",message.qos)
            # print("message retain flag=",message.retain)
            # print('userdata', userdata)
            # print('client', client)

        def on_connect(client, userdata, flags, rc):
            print("Connected with result code "+ str(rc))
            client.subscribe("robots/data")

        self.client.connect_async("localhost",1883,60)
        self.client.on_connect = on_connect
        self.client.on_message = on_message
        await self.client.loop_start()

    async def main(self):
        
        input_coroutines = [self.connect(), self.connect()]
        res = await asyncio.gather(*input_coroutines, return_exceptions=True)

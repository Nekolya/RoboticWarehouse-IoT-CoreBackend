import paho.mqtt.client as mqtt
import asyncio
import json 
from os import environ
from robots.models import Robot, RobotStatus
from zones.models import Area
from users.models import Order

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
            if(message.topic == "robots/data"):
                # print("\nmessage from robot = ", data['area'], ', with id = ', data['id'], sep='')
                print("\nfull data =", data)
                # print("\nmessage topic =",message.topic)
                r = Robot.objects.get(pk=data['id'])
                a = Area.objects.get(pk=data['area'])
                print(r.id, a.id)
                r.area = a
                r.status = RobotStatus.objects.get(pk=data['status'])
                r.save()

                
            if(message.topic == "robots/moving"):
                print("\nfull data =", data)
                print("\nmessage topic =",message.topic)

            if(message.topic == "robots/finish"):
                print("\nfull data =", data)
                print("\nmessage topic =",message.topic)
                o = Order.objects.get(pk=data['order'])
                o.robot = None
                o.save()
                print('\n____________\n')
                
                
            # print("message qos=",message.qos)
            # print("message retain flag=",message.retain)
            # print('userdata', userdata)
            # print('client', client)

        def on_connect(client, userdata, flags, rc):
            print("Connected with result code "+ str(rc))
            client.subscribe("robots/data")
            client.subscribe("robots/moving")
            client.subscribe("robots/finish")

        print(environ.get('MQTT_HOST'), environ.get('MQTT_PORT'), environ.get('MQTT_KEEP_ALIVE'))
        self.client.connect_async(environ.get('MQTT_HOST'), int(environ.get('MQTT_PORT')), int(environ.get('MQTT_KEEP_ALIVE')))
        self.client.on_connect = on_connect
        self.client.on_message = on_message
        await self.client.loop_start()

    async def main(self):
        input_coroutines = [self.connect(), self.connect()]
        res = await asyncio.gather(*input_coroutines, return_exceptions=True)

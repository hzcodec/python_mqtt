# -*- coding: utf-8 -*-

#   Auther      : Heinz Samuelsson
#   Date        : 2018-11-29
#   File        : client_connect.py
#   Reference   : https://www.youtube.com/watch?v=QAaXNt0oqSI
#   Description : -
#   Python ver  : 2.7.3 (gcc 4.6.3)

import paho.mqtt.client as mqtt
import time

def on_log(client, userdata, level, buf):
	print("log:"+buf)

def on_connect(client, userdata, flags, rc):
	if rc == 0:
		print("Connection OK")
	else:
		print("No connection", rc)

def on_disconnect(client, userdata, flags, rc=0):
	print("Disconnected: "+str(rc))

def on_message(client, userdata, msg):
	print("Topic:", msg.topic)
	print("Message:", msg.payload)
	print("QoS:", msg.qos)
	print("Retatin flag:", msg.retain)

#broker = "localhost"
broker = "test.mosquitto.org"

client = mqtt.Client("python1")
client.on_disconnect = on_disconnect
client.on_connect = on_connect
client.on_message = on_message

#client.on_log = on_log

print("Connecting to broker:", broker)

client.connect(broker)

# (topic, qos=0)
client.subscribe("house/sensor1")

client.loop_start()

# (topic, payload=None, qos=0, retain=False)
client.publish("house/sensor1", "My first message")

time.sleep(4)

client.loop_stop()
client.disconnect()

# -*- coding: utf-8 -*-

#   Auther      : Heinz Samuelsson
#   Date        : 2018-11-29
#   File        : publisher_qos2.py
#   Reference   : https://www.youtube.com/watch?v=eY8umQOhClE
#   Description : -
#   Python ver  : 2.7.3 (gcc 4.6.3)

import paho.mqtt.client as mqtt
import time
import logging

broker = "localhost"
#broker = "192.168.1.184"
#port = 1883

# use DEBUG, INFO, WARNING
logging.basicConfig(level=logging.INFO)

def on_log(client, userdata, level, buf):
	logging.info(buf)

def on_connect(client, userdata, flags, rc):
	if rc == 0:
		client.connected_flag = True
		logging.info("Connection OK")
	else:
		logging.info("No connection", rc)
		client.loop_stop()

def on_disconnect(client, userdata, flags, rc=0):
	logging.info("Disconnected: ")

def on_publish(client, userdata, mid):
	logging.info("Mid="+str(mid))

def on_subscribe(client, userdata, mid, granted_qos):
	logging.info("Subscribed")

def on_message(client, userdata, message):
	topic=message.topic
	msgr = str(message.payload.decode("utf-8"))
	logging.info(msgr)

def reset():
	ret = client.publish("house/bulb1", "", 0, True)

mqtt.Client.connected_flag = False

client = mqtt.Client("python1")
client.on_log = on_log
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

#client.connect(broker, port)
client.connect(broker)
client.loop_start()

while not client.connected_flag:
	#print("Wait loop")
	time.sleep(1)

time.sleep(3)
print ("Publishing")

ret = client.publish("house/bulb1", "Test message 0", 0, True)
#print ("Published return=", ret)
time.sleep(3)


ret = client.publish("house/bulb1", "Test message 1", 1)
#print ("Published return=", ret)
time.sleep(3)

ret = client.publish("house/bulb1", "Test message 2", 2)
#print ("Published return=", ret)
time.sleep(3)

client.subscribe("house/bulb1", 2)

time.sleep(10)
client.loop_stop()
client.disconnect()

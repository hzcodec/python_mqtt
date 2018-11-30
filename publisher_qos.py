# -*- coding: utf-8 -*-

#   Auther      : Heinz Samuelsson
#   Date        : 2018-11-29
#   File        : publisher_qos.py
#   Reference   : https://www.youtube.com/watch?v=eY8umQOhClE
#   Description : -
#   Python ver  : 2.7.3 (gcc 4.6.3)

import paho.mqtt.client as mqtt
import time

broker = "localhost"
#broker = "192.168.1.184"
port = 1883

def on_log(client, userdata, level, buf):
	print("log:"+buf)

def on_connect(client, userdata, flags, rc):
	if rc == 0:
		client.connected_flag = True
		print("Connection OK")
	else:
		print("No connection", rc)
		client.loop_stop()

def on_disconnect(client, userdata, flags, rc=0):
	print("Disconnected: "+str(rc))

def on_publish(client, userdata, mid):
	print("Mid=", mid)

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
	print("Wait loop")
	time.sleep(1)

time.sleep(3)
print ("Publishing")

ret = client.publish("house/bulb1", "Test message 0", 0)
print ("Published return=", ret)
time.sleep(3)


ret = client.publish("house/bulb1", "Test message 1", 1)
print ("Published return=", ret)
time.sleep(3)

ret = client.publish("house/bulb1", "Test message 2", 2)
print ("Published return=", ret)
time.sleep(3)

client.loop_stop()
client.disconnect()

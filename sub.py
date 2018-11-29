# -*- coding: utf-8 -*-

#   Auther      : Heinz Samuelsson
#   Date        : 2018-11-29
#   File        : multiprocess1.py
#   Reference   : -
#   Description : Shall be used with pub.py 
#   Python ver  : 2.7.3 (gcc 4.6.3)

import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
	print("Connected with result code "+str(rc))

# Subscribing in on_connect() means that if we lose the connection and
# reconnect then subscriptions will be renewed.
#client.subscribe("hello/world")
client = mqtt.Client("hello/world") 

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	print "Topic: ", msg.topic+'\nMessage: '+str(msg.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)
print 'Client connected'

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

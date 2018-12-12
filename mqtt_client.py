#   Auther      : Heinz Samuelsson
#   Date        : 2018-11-29
#   File        : pub.py
#   Reference   : https://core-electronics.com.au/tutorials/getting-started-with-home-automation-using-mqtt.html
#   Description : MQTT Client demo
#                 Continuously monitor two different MQTT topics for data,
#                 check if the received data matches two predefined 'commands'
#                  
#                 1) Launch mqtt_client in a terminal
#                 2) Launch mqtt_publish in a second terminal

#                    mosquitto_sub -h test.mosquitto.org -t "CoreElectronics/test"
#                    mosquitto_sub -h test.mosquitto.org -t "CoreElectronics/topic"
#                     
#                    mosquitto_pub -d -h test.mosquitto.org -t CoreElectronics/test -m "Hello"
#                    mosquitto_pub -d -h test.mosquitto.org -t CoreElectronics/topic -m "World!"
#
#   Python ver  : 2.7.3 (gcc 4.6.3)

 
import paho.mqtt.client as mqtt
import time
import sys
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	
	# Subscribing in on_connect() - if we lose the connection and
	# reconnect then subscriptions will be renewed.

	if rc == 0:
		client.subscribe("topic_1")
		client.subscribe("topic_2")
		print("Connected with result code "+str(rc))
	else:
		print("No connection")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	print("Topic: "+msg.topic+" "+str(msg.payload))
	
	if msg.payload == "Hello":
	    print("Received message #1")
	    # Do something

	if msg.payload == "World!":
	    print("Received message #2")
	    # Do something else
	
	print(50*'-')

def on_disconnect(client, userdata, flags, rc=0):
	print("Connection disconnected")
 
# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
 
#client.connect("test.mosquitto.org", 1883, 60)
client.connect("localhost", 1883, 60)

# http://www.hivemq.com/demos/websocket-client/
#client.connect("broker.mqttdashboard.com", 8000, 60)
 
# Process network traffic and dispatch callbacks. This will also handle
# reconnecting. Check the documentation at
# https://github.com/eclipse/paho.mqtt.python
# for information on how to use other loop*() functions
client.loop_forever()

#client.loop_start()
#time.sleep(12)
#client.loop_stop()
#client.disconnect()

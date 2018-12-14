#   Auther      : Heinz Samuelsson
#   Date        : 2018-11-29
#   File        : oo_mqtt_client.py
#   Reference   : -
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

class MqttClient():
	def __init__(self):
		print("mqtt client object created\n")
		self.client = mqtt.Client()
		self.client.on_connect = self.on_connect
		self.client.on_message = self.on_message

	def connect_client(self):
		self.client.connect("test.mosquitto.org", 1883, 60)

	def on_connect(self, rc):
        	print("rc: "+str(rc))

	def on_message(self, client, userdata, msg):
		print("Topic: "+msg.topic+" "+str(msg.payload))
		
		if msg.payload == "Hello":
		    	print("Received message #1\n")
			print(50*'-')
	
	def run(self):
		self.client.connect("test.mosquitto.org", 1883, 60)
		self.client.subscribe("topic_1")
	

def on_disconnect(client, userdata, flags, rc=0):
	print("Connection disconnected")
 
# Create an MQTT client and attach our routines to it.
#client = mqtt.Client()
#client.on_connect = on_connect
#client.on_message = on_message
#client.on_disconnect = on_disconnect
# 
##client.connect("test.mosquitto.org", 1883, 60)
#client.connect("localhost", 1883, 60)

# for information on how to use other loop*() functions
#client.loop_forever()

if __name__ == "__main__":
	mqttClient = MqttClient()
	mqttClient.run()


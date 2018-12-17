#   Auther      : Heinz Samuelsson
#   Date        : 2018-12-14
#   File        : oo_mqtt_client.py
#   Reference   : -
#   Description : MQTT Client demo
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

URL = "test.mosquitto.org"
PORT = 1883
KEEP_ALIVE = 60

class MqttClient():
	def __init__(self):
		print("mqtt client object created\n")
		self.client = mqtt.Client()
		self.client.on_connect = self.on_connect
		self.client.on_message = self.on_message

	def on_connect(self, client, port, flag):
        	print("On connect")
		self.client.subscribe("topic_1")

	def on_message(self, client, userdata, msg):
		print("Topic: "+msg.topic+" "+str(msg.payload))
		
		if msg.payload == "Hello":
		    	print("Received message #1\n")
			print(50*'-')
	
	def run(self):
		self.client.on_connect(URL, PORT, KEEP_ALIVE)
		self.client.loop_forever()
	
	def on_disconnect(self, client, userdata, flags, rc=0):
		print("Connection disconnected")
 

if __name__ == "__main__":
	mqttClient = MqttClient()
	mqttClient.run()


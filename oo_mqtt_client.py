#   Auther      : Heinz Samuelsson
#   Date        : 2018-12-14
#   File        : oo_mqtt_client.py
#   Reference   : https://www.hivemq.com/blog/mqtt-client-library-paho-python/
#   Description : MQTT Client demo
#                  
#                 1) Launch oo_mqtt_client in a terminal
#                 2) mosquitto_pub -d -h 10.239.181.182 -t topic_2 -m "Hello"
#                    mosquitto_pub -d -h 192.168.1.239 -t topic_2 -m "Hello"

#   Python ver  : 2.7.3 (gcc 4.6.3)

import paho.mqtt.client as mqtt
import sys

#URL = "test.mosquitto.org"
#URL = "10.239.181.182"
URL = "192.168.1.239"
PORT = 1883
KEEP_ALIVE = 60
TOPIC = "topic_2"
QoS_0 = 0

class MqttClient:

	def __init__(self, master):
		self.master = master
		self.master.on_connect = self.on_connect
		self.master.on_message = self.on_message
		self.master.connect(URL, PORT, KEEP_ALIVE)
		self.master.disconnect = self.on_disconnect

	def on_disconnect(selfm, client, userdata, flags, rc=0):
		print("hello")
	
	def on_connect(self, master, obj, flags, rc):
		self.master.subscribe(TOPIC, qos=QoS_0)
	
	def on_message(self, master, obj, msg):
		print(str(msg.payload))

	def on_disconnect(self):
		print("Disconnected rc="+str(rc))


if __name__ == "__main__":

	client = mqtt.Client()
	mqtt_client_obj = MqttClient(client)
	print("Client started\n")

	try:
		client.loop_forever()

	except KeyboardInterrupt:
		print("\nConnection closed\n")
		#mqtt_client_obj.on_disconnect()
		sys.exit(0)



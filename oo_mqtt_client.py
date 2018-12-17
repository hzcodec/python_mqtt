#   Auther      : Heinz Samuelsson
#   Date        : 2018-12-14
#   File        : oo_mqtt_client.py
#   Reference   : https://www.hivemq.com/blog/mqtt-client-library-paho-python/
#   Description : MQTT Client demo
#                  
#                 1) Launch oo_mqtt_client in a terminal
#                 2) mosquitto_pub -d -h 10.239.181.182 -t topic_2 -m "Hello"

#   Python ver  : 2.7.3 (gcc 4.6.3)

 
import paho.mqtt.client as mqtt

#URL = "test.mosquitto.org"
URL = "10.239.181.182"
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

    def on_connect(self, master, obj, flags, rc):
        self.master.subscribe(TOPIC, qos=QoS_0)

    def on_message(self, master, obj, msg):
        print(str(msg.payload))


if __name__ == "__main__":

	client = mqtt.Client()
	mqtt_client_obj = MqttClient(client)
	client.loop_forever()



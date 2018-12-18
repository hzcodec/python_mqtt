#   Auther      : Heinz Samuelsson
#   Date        : 2018-12-18
#   File        : oo_mqtt_client3.py
#   Reference   : https://github.com/eclipse/paho.mqtt.python/blob/master/examples/client_sub-class.py 
#   Description : MQTT Client demo
#                   mosquitto_pub -d -h 10.239.181.182 -t topic_2 -m "Hello"
#                  
#   Python ver  : 2.7.3 (gcc 4.6.3)

import paho.mqtt.client as mqtt
import sys

class MyMQTTClass(mqtt.Client):

    def on_connect(self, mqttc, obj, flags, rc):
        print("rc: "+str(rc))

    def on_message(self, mqttc, obj, msg):
        print("Topic:"+msg.topic+", QoS="+str(msg.qos)+", Payload:"+str(msg.payload))

    def on_publish(self, mqttc, obj, mid):
        print("mid: "+str(mid))

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: "+str(mid)+" "+str(granted_qos))

    def on_log(self, mqttc, obj, level, string):
        print(string)

    def on_disconnect(self):
	print("\n========================")
	print("Disconnected from broker")
	print("========================")

    def run(self):
        #self.connect("192.168.1.239", 1883, 60)
        self.connect("10.239.181.182", 1883, 60)
        self.subscribe("topic_2", 0)

        rc = 0
	try:
        	while rc == 0:
            		rc = self.loop()
        	return rc

	except KeyboardInterrupt:
		self.on_disconnect()
		sys.exit(0)

mqttc = MyMQTTClass()
rc = mqttc.run()

print("rc: "+str(rc))


# -*- coding: utf-8 -*-

#   Auther      : Heinz Samuelsson
#   Date        : 2018-11-30
#   File        : client_connect2.py
#   Reference   : https://www.youtube.com/watch?v=QAaXNt0oqSI&list=RDQAaXNt0oqSI&start_radio=1
#   Description : -
#   Python ver  : -

import paho.mqtt.client as mqtt
import time

def on_log(client, userdata, level, buf):
	print("log:"+buf)

def on_connect(client, userdata, flags, rc):
	if rc == 0:
		print("    Connection OK")
	else:
		print("    No connection")

def on_disconnect(client, userdata, flags, rc=0):
	print("Disconnected rc="+str(rc))


broker = "test.mosquitto.org"
#broker = "broker.hivemq.com"
#broker = "iot.eclipse.org"

# create an instance
client = mqtt.Client("python1")

# bind callback functions
client.on_connect = on_connect
client.on_log = on_log
client.on_disconnect = on_disconnect

# connect to the broker
print("Connecting to broker", broker)
client.connect(broker)

# start loop - later on stop the loop
client.loop_start()

time.sleep(4)
client.loop_stop()
client.disconnect()


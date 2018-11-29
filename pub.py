# -*- coding: utf-8 -*-

#   Auther      : Heinz Samuelsson
#   Date        : 2018-11-29
#   File        : multiprocess1.py
#   Reference   : -
#   Description : -
#   Python ver  : 2.7.3 (gcc 4.6.3)

import paho.mqtt.client as mqtt

mqttc = mqtt.Client("python_pub")
mqttc.connect("test.mosquitto.org", 1883)
mqttc.publish("hello/world", "Hello World!")

mqttc.loop(2) #//timeout = 2s

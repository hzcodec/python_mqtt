#   Auther      : Heinz Samuelsson
#   Date        : 2018-11-29
#   File        : pub.py
#   Reference   : https://core-electronics.com.au/tutorials/getting-started-with-home-automation-using-mqtt.html
#   Description : MQTT Publish Demo
#                 Publish two messages, to two different topics
#   Python ver  : 2.7.3 (gcc 4.6.3)

import paho.mqtt.publish as publish

publish.single("test", "Hello", hostname="test.mosquitto.org")
publish.single("topic", "World!", hostname="test.mosquitto.org")

print("Done")

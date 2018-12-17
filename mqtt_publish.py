#   Auther      : Heinz Samuelsson
#   Date        : 2018-11-29
#   File        : pub.py
#   Reference   : https://core-electronics.com.au/tutorials/getting-started-with-home-automation-using-mqtt.html
#   Description : MQTT Publish Demo
#                 Publish two messages, to two different topics
#   Python ver  : 2.7.3 (gcc 4.6.3)

import paho.mqtt.publish as publish

HOST_URL = "10.239.181.182"
#publish.single("topic_1", "Hello", hostname="test.mosquitto.org")
#publish.single("topic_2", "World!", hostname="test.mosquitto.org")
publish.single("topic_2", "Hello", hostname=HOST_URL)

print("Done")

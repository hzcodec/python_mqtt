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
#
#   Python ver  : 2.7.3 (gcc 4.6.3)

 
import paho.mqtt.client as mqtt
import time
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("CoreElectronics/test")
    client.subscribe("CoreElectronics/topic")
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    if msg.payload == "Hello":
        print("Received message #1, do something")
        # Do something

    if msg.payload == "World!":
        print("Received message #2, do something else")
        # Do something else
 
# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect("test.mosquitto.org", 1883, 60)
 
# Process network traffic and dispatch callbacks. This will also handle
# reconnecting. Check the documentation at
# https://github.com/eclipse/paho.mqtt.python
# for information on how to use other loop*() functions
client.loop_forever()

#client.loop_start()
#time.sleep(12)
#client.loop_stop()
#client.disconnect()

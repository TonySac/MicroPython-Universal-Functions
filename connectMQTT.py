# Stand alone function to connect Raspberry Pi Pico W to MQTT Server
# **Dependant on active internet connection**
# Uses "secrets.py" to MQTT IDs

import secrets
import mip #Import Micropython package library **Requires internet**
mip.install('umqtt.simple') #Install MQTT package **Requires internet**
from umqtt.simple import MQTTClient

def connectMQTT():
    client = MQTTClient(secrets.mqtt_id, secrets.mqtt_server, keepalive=3600)
    client.connect()
    print('Connected to MQTT Server:', secrets.mqtt_server)
    return client
# Stand alone function to connect Raspberry Pi Pico W to WiFi
# Uses "secrets.py" to store SSID, password, and static IP configurations 

import network
import secrets
from time import sleep

def connectWIFI():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.config(pm = 0xa11140) #Disable Powersave
    wlan.connect(secrets.ssid, secrets.password)
    wlan.ifconfig(secrets.ifconfig)

# Wait for connection to establish
    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            print("Connected to network:", wlan.config('ssid'))
            break
    max_wait -= 1
    sleep(1)

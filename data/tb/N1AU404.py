import time
import paho.mqtt.client as mqtt
import json
import random as random
import pandas as pd

space = pd.read_csv('spaces/N1AU404.csv')

THINGSBOARD_HOST = 'insert TB host domain here'
ACCESS_TOKEN = 'insert acces token for device here'

# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
INTERVAL = 30
sensor_data = dict([(str(name),0) for name in space.columns])
next_reading = time.time() 

client = mqtt.Client()


# Set access token
client.username_pw_set(ACCESS_TOKEN)


# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGSBOARD_HOST, 1883, 60)

client.loop_start()

try:
    i=0
    while True:
        for name in space.columns:
            sensor_data[name] = space[name][i]
    
        # Sending humidity and temperature data to ThingsBoard
        client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)
        i=i+1
 
        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()

import paho.mqtt.client as paho
import time

def on_message(client, userdata, msg):
    print('Topic: {}/{}'.format(msg.topic, msg.payload.decode('utf-8')))

def on_subscribe(client, userdata, mid, granted_qos):
    print('Subscribed: ' + str(mid) + ''+str(granted_qos))


client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect('mqtt.eclipse.org', 1883)

client.subscribe('myhome/+/kitchen')

rc = 0
while rc == 0:
    rc = client.loop()
    time.sleep(2)
#print('Reconnect: ' + str(rc))
from paho.mqtt.client import Client as MC
from paho.mqtt.enums import CallbackAPIVersion
from time import sleep
from random import random
import paho.mqtt.subscribe as subscribe

_mqttc = MC(CallbackAPIVersion.VERSION2)

def callback_func(client, userinfo, message):
    payload_str: str = message.payload.decode()
    if payload_str=='forward':
        print('X=1')
    elif payload_str=='backward':
        print('X=-1')
    elif payload_str=='right':
        print('Y=1')
    elif payload_str=='left':
        print('Y=-1')
    else:
        print('command not found')


def _on_connect(client, userdata, flags, reason_code, properties):
    if reason_code.is_failure:
        print('Failed to connect. Retrying..')
    else:
        print('connected to broker')
        _mqttc.subscribe('robot/move')
        _mqttc.on_message=callback_func


def setup(address = 'localhost', port = 1883):
    _mqttc.on_connect = _on_connect
    _mqttc.connect(address, port)
    _mqttc.loop_start()



setup()

while True:
    sleep(1)
    x = random()
    y = random()
    _mqttc.publish('robot/coordinates', f'{x},{y}')
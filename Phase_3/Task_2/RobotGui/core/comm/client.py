from paho.mqtt.client import Client as MC
from paho.mqtt.enums import CallbackAPIVersion
import paho.mqtt.subscribe as subscribe
import paho.mqtt.publish as publish

import RobotGui.core.comm.sub.coords as coords

_mqttc = MC(CallbackAPIVersion.VERSION2)
flag=False

def _on_connect(client, userdata, flags, reason_code, properties):
    global flag
    if reason_code.is_failure:
        print('Failed to connect. Retrying..')
    else:
        flag=True
        print('connected to broker')
        #subscribe.callback(coords.callback, 'robot/coordinates')
        _mqttc.subscribe('robot/coordinates')
        _mqttc.on_message=coords.callback
        
        

def setup(coords_slot, address = 'localhost', port = 1883):
    coords.slot = coords_slot
    _mqttc.on_connect = _on_connect
    _mqttc.connect(address, port)
    _mqttc.loop_start()

def move_command(message:str):
    if  flag:
        _mqttc.publish('robot/move',message)
    else:
        print('not yet')
    
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class Humidity(Node):
    def __init__(self):
        super().__init__('humidity_node')
        self.publisher_ = self.create_publisher(Int32, 'humidity', 10)
        self.create_timer(2,self.humidity_callback)
        self.num=None

    def humidity_callback(self):
        self.num=random.randint(20,100)
        msg=Int32()  
        msg.data=self.num 
        self.publisher_.publish(msg) 

def main():
    rclpy.init()
    node = Humidity()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
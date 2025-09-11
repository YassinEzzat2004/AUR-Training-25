#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class Temperature(Node):
    def __init__(self):
        super().__init__('temperature_node')
        self.publisher_ = self.create_publisher(Int32, 'temperature', 10)
        self.create_timer(1,self.temperature_callback)
        self.num=None

    def temperature_callback(self):
        self.num=random.randint(15,40)
        msg=Int32()  
        msg.data=self.num 
        self.publisher_.publish(msg) 

def main():
    rclpy.init()
    node = Temperature()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
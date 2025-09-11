#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class Pressure(Node):
    def __init__(self):
        super().__init__('pressure_node')
        self.publisher_ = self.create_publisher(Int32, 'pressure', 10)
        self.create_timer(3,self.pressure_callback)
        self.num=None

    def pressure_callback(self):
        self.num=random.randint(900,1100)
        msg=Int32()  
        msg.data=self.num 
        self.publisher_.publish(msg) 

def main():
    rclpy.init()
    node = Pressure()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
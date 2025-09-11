#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Monitor(Node):
    def __init__(self):
        super().__init__('monitor_node')
        self.temperature = None
        self.humidity = None
        self.pressure = None
        self.log_file = open('sensor_readings.txt', 'a')
        self.temperature_subscription = self.create_subscription(
            Int32,
            'temperature',
            self.temperature_callback,
            10)
        self.humidity_subscription = self.create_subscription(
            Int32,
            'humidity',
            self.humidity_callback,
            10)
        self.pressure_subscription = self.create_subscription(
            Int32,
            'pressure',
            self.pressure_callback,
            10)

    def print_all(self):
        #if (self.temperature!=None)or(self.humidity!=None)or(self.pressure!=None):
        line=f'temp = {self.temperature} C  humidity = {self.humidity} %  pressure = {self.pressure} hPa'
        self.get_logger().info(line)
        self.log_file.write(line+'\n')
        self.log_file.flush()

    def temperature_callback(self, msg:Int32):
        self.temperature=msg.data
        self.print_all()
    def humidity_callback(self, msg:Int32):
        self.humidity=msg.data
        self.print_all()

    def pressure_callback(self, msg:Int32):
        self.pressure=msg.data
        self.print_all()
def main():
    rclpy.init()
    node = Monitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
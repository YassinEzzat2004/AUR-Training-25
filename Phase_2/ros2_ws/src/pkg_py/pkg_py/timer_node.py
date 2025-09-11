import rclpy
from rclpy.node import Node
import time 

class Timer(Node):
    def __init__(self):
        super().__init__('timer_node')

    def countdown(self):
        for i in range(10,-1,-1):
            self.get_logger().info(f'{i}')
            time.sleep(1)

        self.get_logger().info('Time is up!')

def main():
    rclpy.init()
    node=Timer()
    node.countdown()
    node.destroy_node()
    rclpy.shutdown()

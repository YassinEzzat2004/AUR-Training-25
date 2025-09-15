from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim',
            output='screen'
        ),

        Node(
            package='turtle_pkg',
            executable='turtle_chase',
            name='turtle_game',
            output='screen'
        ),
    ])

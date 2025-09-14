from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Run turtlesim_node
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),

        # Run your chase script
        Node(
            package='turtle_chase_pkg',
            executable='turtle_chase',
            name='turtle_chase_node',
            output='screen'
        )
    ])

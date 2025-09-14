from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Start turtlesim GUI
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim',
            output='screen'
        ),

        # Start your custom game node
        Node(
            package='turtle_pkg',
            executable='turtle_chase',
            name='turtle_game',
            output='screen'
        ),
    ])

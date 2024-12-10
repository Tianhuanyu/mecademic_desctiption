from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Get the path to the xacro file
    xacro_file = os.path.join(
        get_package_share_directory('mecademic_description'),
        'urdf',
        'meca_500_r3Robot.urdf.xacro')


    # Robot state publisher node to publish the URDF from the xacro file
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': Command(['xacro ', xacro_file])
        }]
    )
    # Joint state publisher node to publish the joint states
    joint_state_publisher_vis_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher',
        output='screen'
    )

    # RViz node to visualize the robot
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        output='screen'
    )

    return LaunchDescription([
        robot_state_publisher_node,
        rviz_node,
        joint_state_publisher_vis_node,
    ])

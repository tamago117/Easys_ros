import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    package_name = "Easys_ros"

    launch_description_list = []

    #nodes
    joy_node = Node(
            package='joy',
            executable='joy_node',
            )
    launch_description_list.append(joy_node)

    rqt_image_view = Node(
            package='rqt_image_view',
            executable='rqt_image_view',
            )
    launch_description_list.append(rqt_image_view)

    uncompressed_image = Node(
            package='image_transport',
            executable='republish',
            arguments=['compressed', 'in/compressed:=image_raw/compressed', 'raw', 'out:=image_raw/uncompressed'],
            )
    launch_description_list.append(uncompressed_image)
    
    #include yolov8.launch.py
    yolov8_launch_file = os.path.join(
            get_package_share_directory('Easys_ros'),
            'launch',
            'yolov8.launch.py'
            )

    yolov8_launch_cmd = IncludeLaunchDescription(
                PythonLaunchDescriptionSource(yolov8_launch_file),
                launch_arguments={
                'model': 'yolov8s.pt',
                'device': 'cpu', # cuda:0
                'threshold': '0.7',
                }.items(),
                )
    launch_description_list.append(yolov8_launch_cmd)


    return LaunchDescription(launch_description_list)
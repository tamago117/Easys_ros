import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    package_name = "Easys_ros"

    #args
    #filePath = LaunchConfiguration('filePath')

    #parameters
    

    #config
    #rviz_config = os.path.join(get_package_share_directory(
    #    package_name), "config", "rviz", "path_display_2d.rviz")

    #nodes
    joy2cmd = Node(
            package=package_name,
            executable='joy2cmd',)

    Easys_controller = Node(
            package=package_name,
            executable='Easys_controller',
            output='screen',)

    thruster_controller = Node(
            package=package_name,
            executable='thruster_controller',)

    bno055_config = os.path.join(
            get_package_share_directory(package_name),
            'config',
            'bno055_params_i2c.yaml'
            )
    bno055 = Node(
            package="bno055",
            executable="bno055",
            parameters=[bno055_config
            ,],
            remappings=[("/bno055/imu", "imu")],
            )

    v4l2_camera = Node(
            package="v4l2_camera",
            executable="v4l2_camera_node",)


    return LaunchDescription([
        joy2cmd,
        Easys_controller,
        thruster_controller,
        bno055,
        v4l2_camera,
    ])

"""
    <!--<node pkg="bno055" exec="bno055">
        <param name="config" value="$(find Easys_ros)/config/bno055_params_i2c.yaml"/>
    </node>-->
    
    <!--<node pkg="v4l2_camera" exec="v4l2_camera"/>-->
    """
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

    arm_controller = Node(
            package=package_name,
            executable='arm_controller',)

    light_controller = Node(
            package=package_name,
            executable='light_controller',)

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

    ms5837_bar30 = Node(
            package="ms5837_bar_ros",
            executable="bar30_node",
            )

    v4l2_camera = Node(
            package="v4l2_camera",
            executable="v4l2_camera_node",
            parameters=[{
                'image_size': [480, 360]  # ここで画像サイズを指定します（例: 640x480）
            }],
        )


    return LaunchDescription([
        joy2cmd,
        Easys_controller,
        thruster_controller,
        arm_controller,
        light_controller,
        bno055,
        ms5837_bar30,
        v4l2_camera,
    ])
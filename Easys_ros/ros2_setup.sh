#!/bin/bash -e 

apt-get install curl gnupg lsb-release -y
curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null

# install ROS2
apt-get update
apt-get install ros-humble-desktop -y

echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

# make workspace
apt-get install python3-colcon-common-extensions -y
mkdir -p /colcon_ws/src
cd /colcon_ws/ && colcon build

# install dependencies
apt-get install ros-humble-imu-tools -y

# install gazebo
apt-get install gazebo -y
apt-get install ros-humble-gazebo-* -y

source ~/.bashrc
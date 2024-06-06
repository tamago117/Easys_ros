# Setup Raspberry Pi 

## Required Environment
* Raspberry Pi 4 Model B 4GB
* Ubuntu Desktop 22.04 LTS (64-bit) 

## 1. Install ros2 humble

```bash
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
sudo apt install software-properties-common
sudo add-apt-repository universe
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update
sudo apt install ros-humble-desktop
sudo apt install ros-dev-tools
```

## 2. Creating a ROS2 workspace

```bash
ROS_DISTRO=humble
rosdep update
cd $HOME
mkdir -p colcon_ws/src
cd colcon_ws
source /opt/ros/$ROS_DISTRO/setup.bash
colcon build --symlink-install
echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc
echo "source /home/$USER/colcon_ws/install/setup.bash" >> ~/.bashrc
echo "source /home/$USER/colcon_ws/install/local_setup.bash" >> ~/.bashrc
```

## 3. Setup Easys_ros package

```bash
cd $HOME/colcon_ws/src
git clone https://github.com/tamago117/Easys_ros.git
cd ..
colcon build --symlink-install
```

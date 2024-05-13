# Easys_ros
Easys is an open source under water robot. This repository contains hardware and software source(ROS2).

[&rarr; Document Page](https://tamago117.github.io/Easys_ros/)

[&rarr; ICRA2024 Stand-alone Video](https://youtu.be/4HA7E2-nBuU?si=SOEqNSd_vYKx65Tm)

※ **Currently working on an improved version!**
- Add odometry function
- Miniaturization of circuits
- Change to fisheye camera
- improve pressure-resistant cap

![IMG_9673](https://github.com/tamago117/Easys_ros/assets/38370926/150ee971-6230-4fc3-9c5f-c7301954f7d2)
![P8132769](https://github.com/tamago117/Easys_ros/assets/38370926/9c8923b8-014f-4e5c-a402-4565e1488479)

## Hardware
[3D model](https://drive.google.com/drive/folders/1nr-dIgoqMnhwZie1suLELQvrDiUapply?usp=sharing)
### Manufacturing Instruction
- [English ver](documents/ManufacturingInstructions.en.md)
- [日本語](documents/ManufacturingInstructions.ja.md)

## Software
### Environment
- raspberry pi4 (higher than 4Gb RAM)
- ubuntu 22.04
- ROS2 humble

### Installation
```
cd (your workspace)/src
git clone https://github.com/tamago117/Easys_ros.git
colcon build --symlink-install
```

### Usage

```
# robot terminal
ros2 launch Easys_ros Easys_control.launch.py
```
```
# remote PC terminal
ros2 launch Easys_ros remote_control.launch.py
```

## Simulator
[Easys_sim](https://github.com/hrjp/Easys_sim)

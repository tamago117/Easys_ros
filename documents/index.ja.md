--> [English Page](https://tamago117.github.io/Easys_ros/index.html)
# Easys_ros
Easysはオープンソースの水中ロボットです。このリポジトリには、ハードウェアおよびソフトウェアのソース（ROS2）が含まれています。

※ **現在、改良版の開発に取り組んでいます！**

- シミュレータの追加
- オドメトリ機能の追加
- 回路の小型化
- 魚眼カメラへの変更
- 耐圧キャップの改善

![IMG_9673](https://github.com/tamago117/Easys_ros/assets/38370926/150ee971-6230-4fc3-9c5f-c7301954f7d2)
![P8132769](https://github.com/tamago117/Easys_ros/assets/38370926/9c8923b8-014f-4e5c-a402-4565e1488479)

## ハードウェア
[https://drive.google.com/drive/folders/1nr-dIgoqMnhwZie1suLELQvrDiUapply?usp=sharing](https://drive.google.com/drive/folders/1nr-dIgoqMnhwZie1suLELQvrDiUapply?usp=sharing)

## ソフトウェア
### 環境
- Raspberry Pi4（4GB RAM以上）
- Ubuntu 22.04
- ROS2 Humble

### インストール
```
cd (your workspace)/src
git clone https://github.com/tamago117/Easys_ros.git
colcon build --symlink-install
```

### 使用方法

```
# robot terminal
ros2 launch Easys_ros Easys_control.launch.py
```
```
# remote PC terminal
ros2 launch Easys_ros remote_control.launch.py
```
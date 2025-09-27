#!/bin/sh

xhost +local:docker
docker run -it \
           -e DISPLAY=$DISPLAY \
           -v /tmp/.X11-unix:/tmp/.X11-unix \
           -v $HOME/.Xauthority:/root/.Xauthority:rw \
           --net=host \
           --privileged \
           --env="XAUTHORITY=$XAUTH" \
           --shm-size=8g \
           -v $(pwd):/colcon_ws/src/Easys_ros easys
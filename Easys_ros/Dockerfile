# base image 
FROM nvidia/cuda:12.6.0-cudnn-runtime-ubuntu22.04

# environment configuration
ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs
ENV DISPLAY host.docker.internal:0.0
ENV DEBIAN_FRONTEND noninteractive

# set timezone
RUN apt-get update && apt-get install -y tzdata
ENV TZ=Asia/Tokyo 

# build tools
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3 python3-pip
# python tools
RUN apt-get install python3-tk -y

# git
RUN apt-get install git -y

# for windows
RUN apt-get install x11-apps -y

# setup ros2
COPY ros2_setup.sh /root/
RUN bash ~/ros2_setup.sh

# set working directory
WORKDIR /colcon_ws

FROM ros:foxy

RUN apt-get update --fix-missing && \
    apt-get install -y git \
        nano \
        vim \
        python3-pip \
        libeigen3-dev \
        tmux \
        ros-foxy-rviz2 && \
    apt-get -y dist-upgrade && \
    pip3 install transforms3d

RUN git clone https://github.com/f1tenth/f1tenth_gym
RUN cd f1tenth_gym && \
    pip3 install -e .

RUN mkdir -p sim_ws/src/f1tenth_gym_ros
COPY . /sim_ws/src/f1tenth_gym_ros

WORKDIR /sim_ws

RUN . /opt/ros/foxy/setup.sh && \
    apt-get update --fix-missing && \
    rosdep install -i --from-path src --rosdistro foxy -y && \
    colcon build

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
CMD ["/bin/bash"]

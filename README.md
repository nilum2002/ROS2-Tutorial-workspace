## This Repository includes my tutorial workspace in ROS2
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=c%2B%2B&logoColor=white)
![ROS2](https://img.shields.io/badge/ROS2-22314E?style=flat-square&logo=ros&logoColor=white)
![ROS2 Jazzy](https://img.shields.io/badge/ROS2%20Jazzy-22314E?style=flat-square&logo=ros&logoColor=white)
![Makefile](https://img.shields.io/badge/Makefile-427819?style=flat-square&logo=gnu&logoColor=white)




# 🚀 ROS 2 Jazzy Workspace Setup

This repository documents how to set up and run a basic **ROS 2 Jazzy** workspace with `turtlesim`.

---

## 📂 1. Create your ROS workspace

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
```
## ⚙️ 2. Enable colcon autocompletion (recommended)

Add the following line to your bash configuration file:
```bash
echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bashrc
source ~/.bashrc
```
## 🛠️ 3. Build the workspace
Normal build:
```bash
colcon build

```
If you need to override an existing package (e.g., turtlesim):
```bash
colcon build --allow-overriding turtlesim


```
## 🔌 4. Source your workspace

Every time you open a new terminal, run:

    source ~/ros2_ws/install/setup.bash


(Optional but recommended: add this to your ~/.bashrc)

    echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc

## 🐢 5. Run Turtlesim
    
    ros2 run turtlesim turtlesim_node

## Create your own package in ROS2
Preq:

    sudo apt install python3-colcon-common-extensions
    mkdir -p ~/ros2_ws/src
    cd ~/ros2_ws
Navigate to the src:

    cd ~/ros_ws/src
create package:

    ros2 pkg create --build-type ament_cmake --node-name <my_node> <my_pkg>
Build the package form ~/ros_ws:

    colcon build --packages-select my_package

Source:

    source install/local_setup.bash
Run the package:

    ros2 run <my_pkg> <my_node>

## Publisher and Subscriber in C++ 
    

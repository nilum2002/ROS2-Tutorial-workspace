## This Repository includes my tutorial workspace in ROS2


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

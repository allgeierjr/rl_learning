# rl_learning
Ubuntu 18.04 is required 

Prerequisites
python get-pip.py
pip install gitpython
pip install roslibpy

Install Gazebo:
sudo apt-get update
sudo apt-get install gazebo11
Check installation 
gazebo 
Install OpenAI Gym:
pip install Gym 

Download ROS Melodic:
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update
sudo apt install ros-melodic-desktop-full
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
sudo apt install python-rosdep
sudo rosdep init
rosdep update
sudo apt-get install ros-melodic-rqt
sudo apt-get install ros-melodic-rqt-common-plugins
sudo apt-get install ros-melodic-pid
sudo apt-get install ros-melodic-joy 
sudo apt-get install ros-melodic-controller-manager ros-melodic-gazebo-ros-pkgs ros-melodic-gazebo-ros-control ros-melodic-effort-controllers ros-melodic-joystick-drivers ros-melodic-ecl ros-melodic-yocs-controllers ros-melodic-yocs-cmd-vel-mux ros-melodic-kobuki-dock-drive ros-melodic-kobuki-driver ros-melodic-depthimage-to-laserscan

mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
source devel/setup.bash
echo $ROS_PACKAGE_PATH /home/youruser/catkin_ws/src:/opt/ros/melodic/share
sudo apt-get install ros-melodic-ros-tutorials (This step isn’t necessary but can be helpful for those unacquainted with ROS)

Create directory to run training scripts
(within catkin_ws/sr)
catkin_create_pkg rl_learning rospy openai_ros

IF YOU GET THIS ERROR WHILE INSTALLING ROS:
W: GPG error: http://packages.ros.org <YOUR_UBUNTU_VERSION> InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 5523BAEEB01FA116

sudo apt get update 
sudo apt get install
sudo apt-key del 421C365BD9FF1F717815A3895523BAEEB01FA116
sudo -E apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654


Install necessary packages 
cd ~/catkin_ws/src
git clone https://bitbucket.org/theconstructcore/openai_ros.git
cd rl_learning
git clone https://github.com/allgeierjr/rl_learning.git
cd ~/catkin_ws
catkin_make
source devel/setup.bash
rosdep install openai_ros

To run the training simulation (from your catkin_ws directory)
cd config
gedit my_turtlebot2_maze_params.yaml
Edit : ros_ws_abspath: "/home/jen18/catkin_ws" to your path
cd ..
roslaunch rl_training start_training_save.launch

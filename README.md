# TAL-brabo-ros

## Get gripper files 
`git clone https://github.com/utecrobotics/ur5` 


`git clone https://github.com/utecrobotics/robotiq`

## Required packages
Run these command to setup ros control correctly

`sudo apt-get install ros-kinetic-gazebo-ros-pkgs ros-kinetic-gazebo-ros-control`

If you face an error like this 
`[WARN] [1581866907.726842, 173.067000]: Controller Spawner couldn't find the expected controller_manager ROS interface.`

Check if the controllers are correctly installed
` sudo apt-get install ros-kinetic-joint-state-controller
 sudo apt-get install ros-kinetic-effort-controllers
 sudo apt-get install ros-kinetic-velocity-controllers
 sudo apt-get install ros-kinetic-position-controllers
`

### To launch moveit simulation 
`roslaunch brabo_description brabo_bringup_moveit.launch `

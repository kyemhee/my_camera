# The Cheapest Camera in the world

### About the Project
This project mainly focuses on using ROS2
Key functions include 
1. Using a node that publishes camera videos into images
2. Applying different filters by publishing topics
3. Taking screenshots and recording clips through operating the service server and service client.

## Installation

    pip3 install opencv-python
    sudo apt install ros-humble-cv-bridge

## User Guideline

1. Workspace
   First, make a workspace for your project
   
       mkdir -p your_ws_name/src

3. Package
   Then, create a package
   
       ros2 pkg create --build-type ament_python your_package_name

4. Start

   Now start working on the project!

5. Finally

   Open several tabs in the terminal

   Build

       colcon build

   
   Launch

       ros2 launch your_pck_name your_launch_file.py
  
## Parameters


## Nodes(Functions)


# DiffDrive

**DiffDrive** 


# Project Structure
```
 diff_drive
│   ├── config
│   │   ├── gz_bridge.yaml
│   │   ├── mapper.rviz
│   │   ├── mappers_params_online_async.yaml
│   │   ├── nav2_params.yaml
│   │   └── twist_mux.yaml
│   ├── description
│   │   ├── gazebo_control.xacro
│   │   ├── inertial_macros.xacro
│   │   ├── lidar.xacro
│   │   ├── robot_core2.xacro
│   │   ├── robot_core.xacro
│   │   ├── robot_macros.xacro
│   │   └── rover.urdf.xacro
│   ├── diff_drive
│   │   └── __init__.py
│   ├── launch
│   │   ├── description.launch.py
│   │   ├── empty_world.launch.py
│   │   ├── gzsim.launch.py
│   │   ├── localization_launch.py
│   │   └── navigation_launch.py
│   ├── LICENSE
│   ├── package.xml
│   ├── resource
│   │   └── diff_drive
│   ├── setup.cfg
│   ├── setup.py
│   ├── test
│   │   ├── test_copyright.py
│   │   ├── test_flake8.py
│   │   └── test_pep257.py
│   └── worlds
│       ├── empty.world
│       └── random.sdf
├── training
│   ├── LICENSE
│   ├── package.xml
│   ├── resource
│   │   └── training
│   ├── setup.cfg
│   ├── setup.py
│   ├── test
│   │   ├── test_copyright.py
│   │   ├── test_flake8.py
│   │   └── test_pep257.py
│   └── training
│       ├── client.py
│       ├── __init__.py
│       ├── publisher.py
│       ├── __pycache__
│       │   ├── client.cpython-310.pyc
│       │   ├── __init__.cpython-310.pyc
│       │   ├── publisher.cpython-310.pyc
│       │   ├── service.cpython-310.pyc
│       │   └── subscriber.cpython-310.pyc
│       ├── service.py
│       └── subscriber.py
└── training_interfaces
    ├── CMakeLists.txt
    ├── include
    │   └── training_interfaces
    ├── LICENSE
    ├── msg
    │   └── Person.msg
    ├── package.xml
    ├── src
    └── srv
        └── Value.srv


```

# Softwares used  : 

| Name | Version | link for referene | 
|------|---------|-------------------|
| Ros2 | Humble | [install ros2 humble](https://docs.ros.org/en/humble/Installation.html) |
| ignitiion gazebo | fortress | [install](https://gazebosim.org/docs/fortress/install/) |

# Toolboxes used : 

| Name | link for reference | 
|------|--------------------|
| SLAM Toolbox | [slam_toolbox](https://github.com/SteveMacenski/slam_toolbox) |
| Nav2 Stack | [Nav2](https://roboticsbackend.com/ros2-nav2-generate-a-map-with-slam_toolbox/) |

# Installation

1). Create a Worspace with an src folder:

```
mkdir dd_ros
cd dd_ros
mkdir src 

```
2). in the src folder, clone contents of the github into the folder

```
git clone https://github.com/AkshayArjun/DiffDrive.git

```

3). Install dependencies: 

```
rosdep install --from-paths src -y --ignore-src
```

4). colcon build it from workspace folder, then source it: 

```
colcon build --symlink-install
source install/setup.bash

```

# Featueres : 

| prefix | fnction | pkg | file | description| 
|--------| ------- |-----|------|------------|
|ros2 | launch | diff_drive | empty_world.launch.py | Opens a world with obstacles and the bot (to check if everything is working fine) | 
| ros2 | launch | diff_drive | localization_launch.py | runs the localisation algorithmn which will be later used for nav2 | 
| ros2 | launch | diff_drive | navigateion_launch.py | runs nav2 stack that takes care of obstacle avoidance | 
|||||
| ros2 | run | training | listner | starts the listener node | 
| ros2 | run | training | talker | startst he talker node that publishes using the mesasge type "Person" | 
| ros2 | run | training | clinet {insert num 1 } { insert num 2 } | starts a client and waits for the service to be active | 
| ros2 | run | training | service | takes the client arguements and returns their sum | 

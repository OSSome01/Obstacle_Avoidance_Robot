# Obstacle Avoidance Robot Simulation  

_Building a differential drive robot which can avoid obstacles. The robot design and other requirements can be found in this [PDF](https://github.com/OSSome01/Obstacle_Avoidance/blob/master/Problem_Statement.pdf)._  
This work was done taking reference from [here](https://www.theconstructsim.com/ros-projects-exploring-ros-using-2-wheeled-robot-part-1).

## Prerequisites  

* [ROS](http://wiki.ros.org/kinetic)  
* [Gazebo](http://wiki.ros.org/gazebo_ros_pkgs)

## Getting Started

1. Clone this repository.
2. Run `catkin_make` for both `catkin_ws` and `simulation_ws`.
3. Run 'source catkin_make/devel/setup.bash' and 'source simulation_ws/devel/setup.bash'
3. Launch your terminal and run the command `roslaunch my_worlds <world_name>.launch`. 
This will launch the gazebo enviroment
4. In another terminal, run the command `roslaunch obst_avoidance_robot_description spawn.launch`. 
This will load the robot in the environment at origin. It can be spawned at different location by giving additional arguments like `x:=1 y:=2 z:=3.  
5. In another terminal run `rosrun motion_plan obstacle_avoidance.py`. This will start the robot and obstacle avoidance algorithm.

## Video

[![obstacle-avoidance-bot-using-ros-and-gazebo](https://img.youtube.com/vi/0pR6Cr7dMHA/0.jpg)](https://youtu.be/0pR6Cr7dMHA "obstacleAvoidanceRobot")

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

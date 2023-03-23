# UAV-Precision-Landing
**Aim**: Landing of a 6 rotor drone on a moving target using ARUCO marker vi sensing and depth estimation.

**Description**: This repository contains code for autonomous precision landing for Unmanned Aerial Vehicles on a moving platform. It has been simulated and tested on ROS-Noetic with the help of RotorS Simulator developed by ETH-ASL. The framework works on the basis of detecting an AR marker in the vicinity, estimating the position of the marker and finally planning its approach for landing.

**Dependencies**
1. rotors_simulator by ETH-ASL
2. opencv-contrib-python
3. Klampt
4. stereo_image_proc

**Citations**

1. rotors_simulator:

Fadri Furrer, Micheal Burri, Markus Achtelik, and Roland Siegwart, "RotorS---A Modular Gazebo MAV Simulator Framework in Robot Operating System (ROS): The Complete Reference (Volume 1)", pages: 595--625. In "Springer International Publishing" 2016.

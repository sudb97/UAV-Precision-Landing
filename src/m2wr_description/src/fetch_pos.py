#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
import yaml


def callback(msg):
    f = open("/home/sudarshan/mav_precision_landing/src/m2wr_description/src/pose.txt", "w")
    f.write(str(msg.pose.pose))
    #print( type(msg.pose.pose))
    f.close()

if __name__ == '__main__':
    rospy.init_node('check_odometry')
    odom_sub = rospy.Subscriber('/odom', Odometry, callback)
    rospy.spin()
#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

import pygame
pygame.init()


win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Platform Controler")

def talker():
    msg = Twist()
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz


    run = True
    while run:
        
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_LEFT]:
            msg.linear.x = 0
            msg.linear.y = 0
            msg.angular.z = -1
            pub.publish(msg)
            continue

        if keys[pygame.K_RIGHT]:
            msg.linear.x = 0
            msg.linear.y = 0
            msg.angular.z = 1
            pub.publish(msg)   
            continue    

        if keys[pygame.K_UP]:
            msg.linear.x = 0.5
            msg.linear.y = 0
            msg.angular.z = 0
            pub.publish(msg)    
            continue

        if keys[pygame.K_DOWN]:
            msg.linear.x = -0.5
            msg.linear.y = 0
            msg.angular.z = 0
            pub.publish(msg)
            continue

        msg.linear.x = 0
        msg.linear.y = 0
        msg.angular.z =0
        pub.publish(msg) 
        
        pygame.display.update() 

        rate.sleep()
    
    pygame.quit()




if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
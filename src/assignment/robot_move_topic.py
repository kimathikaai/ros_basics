#!/usr/bin/env python
# Every Python ROS Node with have this declaration at the top
# The first line makes sure your script is executed as a Python script

import rospy
# from std_msgs.msg import String
from geometry_msgs.msg import Twist

def move():
    speed_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('move', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
    	twist = Twist()
    	twist.linear.x = 2.0
    	twist.angular.z = 2.0

        rospy.loginfo(twistmove_msg)
        speed_publisher.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass

# Subscriber for the topic that will show the location of the robot

# Publisher to topic that will make the robot move

# What is the topic of the positon
# What is the topic that makes the robot moves
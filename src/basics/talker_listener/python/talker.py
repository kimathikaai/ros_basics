#!/usr/bin/env python
# Every Python ROS Node with have this declaration at the top
# The first line makes sure your script is executed as a Python script

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The 
    # anonymous=True flag means that rospy will choos a unique
    # name for our 'talker' node
    rospy.init_node('talker', anonymous=True)
    #set loop rate
    rate = rospy.Rate(10) # 10hz
    # keep publishing unitl Ctr-C is pressed
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
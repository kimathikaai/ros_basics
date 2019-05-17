#!/usr/bin/env python

import sys
import rospy
from beginner_tutorials.srv import *

def add_two_ints_client(x, y):
	# For clients you don't have to call init_node()
	# This method blocks execution while waiting for a 
	# service called 'add_two_ints' to be available
    rospy.wait_for_service('add_two_ints')
    try:
    	# We can use this handle just like a normal function
        # The return value us an AddTwoIntsResponse object
        # if the call fails, rospy.ServiceException is called
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        resp1 = add_two_ints(x, y)
        return resp1.sum
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print usage()
        sys.exit(1)
    print "Requesting %s+%s"%(x, y)
    print "%s + %s = %s"%(x, y, add_two_ints_client(x, y))
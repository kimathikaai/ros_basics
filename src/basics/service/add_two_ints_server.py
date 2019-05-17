#!/usr/bin/env python

from beginner_tutorials.srv import *
import rospy

def handle_add_two_ints(req):
	sum = req.a + req.b
	print "Returning [{} + {} = {}]".format(req.a, req.b, sum)
	return AddTwoIntsResponse(sum)

def add_two_ints_server():
	# Initialize and declare node
	rospy.init_node('add_two_ints_server')
	# Declare service
	s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
	print("Ready to add two ints.")
	# Keeps code from exiting until the service is shutdown
	rospy.spin()

if __name__ == "__main__":
	add_two_ints_server()
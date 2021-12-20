#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16

def callback(data):
	if data.data%2 == 0:
		rospy.loginfo(data.data)

if __name__ == '__main__':
	rospy.init_node('left_encoder_ticks_sub', anonymous = True)
	rospy.Subscriber("left_ticks", Int16, callback)
	rospy.spin()

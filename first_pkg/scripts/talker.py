#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16
left_encoder_tics = 0

def talker():
	global left_encoder_tics

	rate = rospy.Rate(100) # 10hz
	while not rospy.is_shutdown():
		rospy.loginfo(left_encoder_tics)
		pub.publish(left_encoder_tics)
		left_encoder_tics +=1
		rate.sleep()

if __name__ == '__main__':
	pub = rospy.Publisher("left_ticks", Int16, queue_size=1)
	rospy.init_node('left_encoder_ticks_node', anonymous=True)
	try:
		talker()
	except rospy.ROSInterruptException:
		pass

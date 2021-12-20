#!/usr/bin/env python

import rospy
from obs_svce.srv import svce_eg, svce_egResponse

def turn_on_off(light):
	if light.flag==1:
		print("Starting Obstacle avoidance service")
		return svce_egResponse('ON')
	else:
		print("Stopping Obstacle avoidance service")
		return svce_egResponse('OFF')


rospy.init_node('service_response')
rospy.loginfo('OBSTACLE SERVICE - SERVER STARTED')

service = rospy.Service('service_obs', svce_eg, turn_on_off)

rospy.spin()

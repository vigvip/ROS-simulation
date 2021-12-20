#!/usr/bin/env python

import rospy

from obs_svce.srv import svce_eg

import sys

rospy.init_node('client_call')

rospy.wait_for_service('service_obs')

srv=rospy.ServiceProxy('service_obs', svce_eg)

result=srv(0)

print(result)

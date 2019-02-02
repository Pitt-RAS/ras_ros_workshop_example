#!/usr/bin/env python

import rospy

if __name__ == '__main__':
    rospy.init_node('test_node')

    while not rospy.is_shutdown():
        rospy.logwarn_throttle(1, 'My first node!')

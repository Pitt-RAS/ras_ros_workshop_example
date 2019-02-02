#!/usr/bin/env python

import rospy

from std_msgs.msg import String

def callback(msg):
    rospy.logwarn(msg.data)


if __name__ == '__main__':
    rospy.init_node('sub_node')

    rospy.Subscriber('example_topic', String, callback)

    rospy.spin()

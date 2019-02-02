#!/usr/bin/env python

import rospy

from std_msgs.msg import String

if __name__ == '__main__':
    rospy.init_node('pub_node')

    rospy.logwarn('My first publisher node!')

    rate = rospy.Rate(5)

    pub = rospy.Publisher('example_topic', String, queue_size=10)

    while not rospy.is_shutdown():
        msg = String()
        msg.data = 'I can publish!'

        pub.publish(msg)

        rate.sleep()

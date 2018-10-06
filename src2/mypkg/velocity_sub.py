#!/usr/bin/env python
#This line is very important


"""
Intro goes here
"""

import rospy
from nav_msgs.msg import Odometry

def callback(data):
    """
    Callback does something everytime a message is recieved by a subscriber.
    You define the logic after this line.
    :params:
    data: this is the data processed by the callback
    :return: returns nothing
    """
    print(data.twist.twist)
    print(data.pose.pose)
    

def subscribe(topic_name='/odom', callback_name=callback, node_name="vel_sub_node", message_object=Odometry):
    rospy.init_node(node_name, anonymous=True)
    rospy.Subscriber(topic_name, message_object, callback_name)
    rospy.spin() # keeps the subscriber process from dying.

def main():
    """
    You can begin by modifying this function.
    """
    subscribe()

if __name__=="__main__":
    main()

#!/usr/bin/env python
#This line is very important


"""
Intro goes here
"""

import rospy
from sensor_msgs.msg import PointCloud

def sonarCallback(data):
    """
    Callback does something everytime a message is recieved by a subscriber.
    You define the logic after this line.
    :params:
    data: this is the data processed by the callback
    :return: returns nothing
    """

    pointNum = 0
    for point in data.points:
        print("Sensor #" + str(pointNum) + "\nValue:\n" + str(point))
        pointNum += 1


def sonarSub(topic_name='/sonar', callback_name=sonarCallback, node_name="sonar_sub_node", message_object=PointCloud):
    rospy.init_node(node_name, anonymous=True)
    rospy.Subscriber(topic_name, message_object, callback_name)
    rospy.spin() # keeps the subscriber process from dying.

def main():
    """
    You can begin by modifying this function.
    """
    sonarSub()

if __name__=="__main__":
    main()

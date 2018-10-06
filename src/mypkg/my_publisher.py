#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

cmd_vel_pub = {}

def circle(x,wz):
    """
    This function sets your speed for the publisher. Use this function to implement your ideas.
    :params:
    x:This is the velocity along x-axis in m/sec. Limits: [-0.3,0.3]
    y:This is the velocity along y-axis in m/sec. Limits: [-0.3,0.3]
    wz: This is the angular velocity for turning (yaw) in rad/sec. Limits: [-1,1]
    :return: Returns a speed message
    """
    speed = Twist()
    speed.linear.x = 1
    speed.linear.y = 0
    speed.linear.z = 0
    speed.angular.x = 0
    speed.angular.y = 0
    speed.angular.z = 1
    cmd_vel_pub(speed)

def publish_circle():
    global cmd_vel_pub
    """
    :params:
    speed_msg: this is the speed message coming from the set_speed function
    topic: this is the topic name you publish to
    msg_type: this is the message type
    node_name: this is the name of your node
    :return: returns nothing
    """

    #Initialize your node & publisher here.
    rospy.init_node(node_name, anonymous=True)
    cmd_vel_pub = rospy.Publisher("/cmd_vel", twist)
    rate = rospy.Rate(10)

    #Publish till your node is running
    while not rospy.is_shutdown():
        circle()

def main():
    """
    This is the main function. Implement your logic here.
    :params: No params
    :return: returns nothing
    """
    publish_circle(msg)

if __name__=="__main__":
    main()

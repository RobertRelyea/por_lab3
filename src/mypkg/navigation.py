#!/usr/bin/env python
#This line is very important

import rospy
from sensor_msgs.msg import PointCloud
from geometry_msgs.msg import Twist
import math

points = []

cmd_vel_pub = {}

def sonarCallback(data):
    global points
    """
    Callback does something everytime a message is recieved by a subscriber.
    You define the logic after this line.
    :params:
    data: this is the data processed by the callback
    :return: returns nothing
    """
    points = data.points
    

def sonarSub(topic_name='/sonar', callback_name=sonarCallback, node_name="sonar_sub_node", message_object=PointCloud):
    global cmd_vel_pub
    rospy.init_node(node_name, anonymous=True)
    rospy.Subscriber(topic_name, message_object, callback_name)
    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(10)

    while(not rospy.is_shutdown()):
        get_vel(points)
        rate.sleep()

def get_vel(points):
    global cmd_vel_pub
    net_z = 0
    for point in points:
        x = point[0]
        y = point[1]
        net_z += (10 - math.sqrt(x*x + y*y)) * (math.atan2(y,x))
        
    print(net_z)
    cmd_vel = Twist()
    cmd_vel.linear.x = 0.2
    cmd_vel.angular.z = net_z / 20


    cmd_vel_pub.publish(cmd_vel)


def main():
    """
    You can begin by modifying this function.
    """
    sonarSub()

if __name__=="__main__":
    main()

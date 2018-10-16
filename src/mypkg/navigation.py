#!/usr/bin/env python
#This line is very important

import rospy
from sensor_msgs.msg import PointCloud
from geometry_msgs.msg import Twist
import math
import pdb

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
    global cmd_vel_pub, points
    rospy.init_node(node_name, anonymous=True)
    rospy.Subscriber(topic_name, message_object, callback_name)
    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(10)

    while(not rospy.is_shutdown()):
        get_vel()
        rate.sleep()

def get_vel():
    global cmd_vel_pub, points
    net_z = 0
    # for i in range(len(points)):
    #     x = points[i].x
    #     y = points[i].y
    #     net_z += (10 - math.sqrt(x*x + y*y)) * (math.atan2(y,x))

    left_turn = 0
    right_turn = 0
    linear = 0

    if len(points) == 8:

        for i in range(3):
            x = points[i].x
            y = points[i].y
            right_turn += 10 - math.sqrt(x*x + y*y)

        for i in range(3,6):
            x = points[i].x
            y = points[i].y
            left_turn += 10 - math.sqrt(x*x + y*y)
        


        net_z = left_turn - right_turn

        dist2 = math.sqrt(points[2].x * points[2].x + points[2].y * points[2].y)
        dist3 = math.sqrt(points[3].x * points[3].x + points[3].y * points[3].y)
        

        if (dist2 < 0.5 or dist3 < 0.5):
            linear = 0
        else:
            linear = 0.2

        print(net_z)
        cmd_vel = Twist()
        cmd_vel.linear.x = linear
        cmd_vel.angular.z = net_z / 5


        cmd_vel_pub.publish(cmd_vel)


def main():
    """
    You can begin by modifying this function.
    """
    sonarSub()

if __name__=="__main__":
    main()

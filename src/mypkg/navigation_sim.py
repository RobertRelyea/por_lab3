#!/usr/bin/env python
#This line is very important

import sensor_msgs.point_cloud2 as pc2
import rospy
from sensor_msgs.msg import PointCloud2, LaserScan
import laser_geometry.laser_geometry as lg
from geometry_msgs.msg import Twist
import math
import numpy as np

lp = lg.LaserProjection()
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
    # convert the message of type LaserScan to a PointCloud2
    pc2_msg = lp.projectLaser(data)

    # listener.transformPointCloud2('/odom', pc2_msg)
    
    # convert it to a generator of the individual points
    point_generator = pc2.read_points(pc2_msg)



    pointNum = 0
    points = []
    for point in point_generator:
        if pointNum % 30 == 0:
            points.append(point)
            # print(point)
        pointNum += 1

# def sonarSub(topic_name='/sonar', callback_name=sonarCallback, node_name="sonar_sub_node", message_object=PointCloud):
def sonarSub(topic_name='/scan', callback_name=sonarCallback, node_name="sonar_sub_node", message_object=LaserScan):
    global cmd_vel_pub
    rospy.init_node(node_name, anonymous=True)
    rospy.Subscriber(topic_name, message_object, callback_name)
    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(10)

    while(not rospy.is_shutdown()):
        # print(len(points))
        # decay_grid()
        # add_points(points)
        get_vel(points)
        rate.sleep()

# def add_points(points, transformer):
#     global grid

#     # Grab transform from points to odom

#     # Calculate grid coords for points

#     # Add points to grid

# def decay_grid():
#     global grid

#     # Decrement values in grid by 1
#     grid = grid - 1

def get_vel(points):
    global cmd_vel_pub
    net_x = 0.2
    net_y = 0
    for point in points:
        x = point[0]
        y = point[1]
        net_y += (10 - math.sqrt(x*x + y*y)) * (math.atan2(y,x))
        
    print(net_y)
    cmd_vel = Twist()
    cmd_vel.linear.x = net_x
    cmd_vel.angular.z = net_y / 20


    cmd_vel_pub.publish(cmd_vel)


def main():
    """
    You can begin by modifying this function.
    """
    sonarSub()

if __name__=="__main__":
    main()

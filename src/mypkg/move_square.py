#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist, Quaternion
from nav_msgs.msg import Odometry
import tf

cmd_vel_pub = {}
linear_x = 0
linear_y = 0
angular = 0


def callback(data):
    global linear_x, linear_y, angular
    """
    Callback does something everytime a message is recieved by a subscriber.
    You define the logic after this line.
    :params:
    data: this is the data processed by the callback
    :return: returns nothing
    """
    quaternion = (
        data.pose.pose.orientation.x,
        data.pose.pose.orientation.y,
        data.pose.pose.orientation.z,
        data.pose.pose.orientation.w)


    # if prev_pos != 0:
    #     linear += data.pose.pose.position.x - prev_pos
    #     new_ang = tf.transformations.euler_from_quaternion(quaternion)
    #     angular += new_ang[2] - prev_ang



    linear_x = data.pose.pose.position.x
    linear_y = data.pose.pose.position.y
    angular = tf.transformations.euler_from_quaternion(quaternion)[2]

    
    

def init_square(topic_name='/pose', callback_name=callback, node_name="vel_sub_node", message_object=Odometry):
    global cmd_vel_pub, linear_x, linear_y, angular

    #Initialize your node & publisher here.
    rospy.init_node("square_move_node", anonymous=True)
    rospy.Subscriber(topic_name, message_object, callback_name)
    cmd_vel_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(100)

    #Publish till your node is running
    stop_msg = Twist()
    while not rospy.is_shutdown():
        
        cmd_vel_pub.publish(stop_msg)
        # Move forward 1 meter
        while linear_x < 1:
            msg = Twist()
            msg.linear.x = 1
            cmd_vel_pub.publish(msg)
            rate.sleep()

        cmd_vel_pub.publish(stop_msg)
        rate.sleep()

        while angular < 1.57:
            msg = Twist()
            msg.angular.z = 1
            # print(angular)
            cmd_vel_pub.publish(msg)
            rate.sleep()

        while linear_y < 1:
            msg = Twist()
            msg.linear.x = 1
            cmd_vel_pub.publish(msg)
            rate.sleep()

        while angular < 3:
            msg = Twist()
            msg.angular.z = 1
            # print(angular)
            cmd_vel_pub.publish(msg)
            rate.sleep()

        while linear_x > 0:
            msg = Twist()
            msg.linear.x = 1
            cmd_vel_pub.publish(msg)
            rate.sleep()

        cmd_vel_pub.publish(stop_msg)
        rate.sleep()

        while abs(angular) > 1.57:
            msg = Twist()
            msg.angular.z = 1
            # print(angular)
            cmd_vel_pub.publish(msg)
            rate.sleep()

        while linear_y > 0:
            msg = Twist()
            msg.linear.x = 1
            cmd_vel_pub.publish(msg)
            rate.sleep()

        while abs(angular) > 0.1:
            msg = Twist()
            msg.angular.z = 1
            # print(angular)
            cmd_vel_pub.publish(msg)
            rate.sleep()




def main():
    """
    This is the main function. Implement your logic here.
    :params: No params
    :return: returns nothing
    """
    init_square()

if __name__=="__main__":
    main()

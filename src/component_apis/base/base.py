#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Header

HUSKY_BASE_TOPIC = '/cmd_vel'
FRAME_ID = 'base_link'
DEFAULT_SEQ_NUM = 0

class BaseNode():
    def __init__(self):
        self.base_pub = rospy.Publisher(HUSKY_BASE_TOPIC, Twist, queue_size=10)

class LinearVelocity():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class AngularVelocity():
    def __init__(self, x, y, z, w):
        self.x = x 
        self.y = y
        self.z = z

def create_base_msg(lin_vel, ang_vel):
    msg = Twist()
    fill_lin_vel(msg, lin_vel)
    fill_ang_vel(msg, ang_vel)
    return msg

def fill_header(msg):
    msg.target_pose.header = Header()
    msg.target_pose.header.seq = DEFAULT_SEQ_NUM
    msg.target_pose.header.stamp = rospy.Time(0)
    msg.target_pose.header.frame_id = FRAME_ID

def fill_lin_vel(msg, lin_vel):
    msg.linear.x = lin_vel.x
    msg.linear.y = lin_vel.y
    msg.linear.z = lin_vel.z

def fill_ang_vel(msg, ang_vel):
    msg.angular.x = ang_vel.x
    msg.angular.y = ang_vel.y
    msg.angular.z = ang_vel.z

def publish_base_message(publisher, position, orientation):
    msg = create_base_msg(position, orientation)
    print(msg, publisher)
    publisher.publish(msg)

""" 
    From Clearpath Documentation 
    Set the linear.x value to drive the 
    robot forwards or backwards, and the angular.z value to rotate left or right.
"""

def TURN(publisher):
    lin_vel = LinearVelocity(0, 0, 0)
    ang_vel = AngularVelocity(0, 0, 0.1)
    publish_base_message(publisher, lin_vel, ang_vel)

def FORWARD(publisher):
    lin_vel = LinearVelocity(0.1, 0, 0)
    ang_vel = AngularVelocity(0, 0, 0)
    publish_base_message(publisher, lin_vel, ang_vel)

def STOP(publisher):
    lin_vel = LinearVelocity(0, 0, 0)
    ang_vel = AngularVelocity(0, 0, 0)
    publish_base_message(publisher, lin_vel, ang_vel)
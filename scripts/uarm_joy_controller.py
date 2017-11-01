#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tatsuya Ishikawa <itatsuya@vt.edu>

import rospy
from sensor_msgs.msg import Joy
import pyuarm

def callback(msg):
    x = msg.axes[2] # right stick horizontal
    y = msg.axes[3] # right stick vertical
    z = ((1 - msg.axes[16]) - (1 - msg.axes[18])) / 2 # tri, x

def uarmJoyController():
    rospy.init_node('uarm_joy_controller', anonymous=True)
    rospy.Subscriber('/joy', Joy, callback)

if __name__ == '__main__':
    listener()

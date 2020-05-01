#!/usr/bin/env python
# coding: utf-8
import rospy
from ik import *
from numpy import interp
from time import sleep
from dynamixel_sdk import *
from ros_falcon.msg import *
from dxl.dxlchain import DxlChain

global motores
motores = DxlChain("/dev/ttyUSB0", rate = 1000000)
motors = motores.get_motor_list()
#print motors

def callback_function(data):
    X = 0 #-100+(data.X-(-52))*1.8518
    Y = 0 #-150+(data.Y-(-53))*
    Z = -400 + (data.Z-(50))*-2.1
    ri = inverse(X, Y, Z)
    motor1 = int(round(3800 - 10.8888*ri[0]))
    motor2 = int(round(3050 - 11.8888*ri[1]))
    motor3 = int(round(2350 - 11.4444*ri[2]))
    #motores.goto(1, motor1, speed = 20, blocking = False) 
    #motores.goto(2, motor2, speed = 20, blocking = False)
    #motores.goto(3, motor3, speed = 20, blocking = False) 
    #sleep(2)
    print motor1, motor2, motor3
    #print motores.get_position()
    #print "{:.4f}, {:.4f}, {:.4f} ".format(X,   Y,   Z) 

rospy.init_node('tele_remota', anonymous=True) 
rospy.Subscriber("/falconPos", falconPos, callback_function) 
rospy.spin()



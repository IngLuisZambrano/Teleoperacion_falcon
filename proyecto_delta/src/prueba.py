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

def principal():
    pub = rospy.Publisher('prueba', falconPos, queue_size=10) 
    rospy.init_node('publicador_prueba', anonymous=True) #inicia el nodo publicador
    rate = rospy.Rate(0.5) # 0.5 Hz
    X = 0#-100+(56-(-56))*-1.8518
    Y = 0
    Z = -400+(-50-(50))*-2.1
    ri = inverse(X, Y, Z)
    motor1 = int(round(3800 - 10.8888*ri[0]))
    motor2 = int(round(3050 - 11.8888*ri[1]))
    motor3 = int(round(2350 - 11.4444*ri[2]))
    motores.goto(1, motor1, speed = 20, blocking = False) 
    motores.goto(2, motor2, speed = 20, blocking = False)
    motores.goto(3, motor3, speed = 20, blocking = False) 
    print motor1, motor2, motor3

if __name__ == '__main__':
    try:
        principal()
    except rospy.ROSInterruptException:
	pass 




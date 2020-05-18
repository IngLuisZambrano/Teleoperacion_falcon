#!/usr/bin/env python
import rospy
import numpy as np
import pandas as pd
from ros_falcon.msg import *
import matplotlib.pyplot as plt
from dxl.dxlchain import DxlChain


global motores, c, datos, df, datos
datosx = []
datosy = []
datosz = []
datos = []
c = 0
motores = DxlChain("/dev/ttyUSB0", rate = 1000000)
motors = motores.get_motor_list()
#print motors


def callback_function(data): 
    global c, df, datos
    data1 = int(data.X)
    data2 = int(data.Y)
    data3 = int(data.Z)
    datosx.append(data1)
    datosy.append(data2)
    datosz.append(data3)
    datos = {'Pos_Fx': datosx, 'Pos_Fy': datosy, 'Pos_Fz': datosz}
    #df = pd.DataFrame(datos, columns = ['Pos_Fx','Pos_Fy','Pos_Fz'])
    #df.to_excel('Datos23.xlsx', sheet_name = 'Datos')

    #print c
    c = c + 1
    if c>40:
    	motores.goto(1, data.X, speed = 40, blocking = False) 
    	motores.goto(2, data.Y, speed = 40, blocking = False)
    	motores.goto(3, data.Z, speed = 40, blocking = False)
        c = 0
    #print data.X, data.Y, data.Z, data1, data2, data3


def publisher(): 
    global datos, df
    rospy.init_node('subs_falcon', anonymous=True)
    rospy.Subscriber("/ir_pos", falconPos, callback_function)
    rospy.spin()

if __name__ == '__main__':
    publisher()







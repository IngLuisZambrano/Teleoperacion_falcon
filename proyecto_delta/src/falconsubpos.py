#!/usr/bin/env python
# coding: utf-8
import rospy 
from ik import * 
import tkMessageBox  
from Tkinter import *  
from dynamixel_sdk import *                    
from ros_falcon.msg import *         
from dxl.dxlchain import DxlChain
from proyecto_delta.msg import posicion

global x,y,z, data, td1

def callback_function(data): 
    print("X: ",data.X)
    print("Y: ",data.Y)
    print("Z: ",data.Z)

def publisher():   
    global x,y,z                                                                  #funcion principal del nodo
    rospy.init_node('falconluis', anonymous=True)                                 #inicializa nodo con nombre subscriptor
    s = rospy.Subscriber("/falconPos", falconPos, callback_function)

    # Ventana Raiz - Principal
    vp = Tk()
    vp.title("Teleoperación Remota")
    vp.geometry("400x200+0+0")
    vp.resizable(0, 0)
    # Configuración de Frame1
    frame1 = Frame(vp, width = 400, height = 400 )
    frame1.pack(side = "left", anchor = "n")
    frame1.config(bg="#86f1ef", cursor="hand2")

    tc3 = Label(frame1, bg = "#86f1ef")
    tc3.grid(row = 0, column = 0, padx = 2, pady = 1)
    tc4 = Label(frame1, bg = "#86f1ef")
    tc4.grid(row = 14, column = 0, padx = 2, pady = 1)

    te1 = Label(frame1, text = "Px", bg = "#86f1ef", font=("Comic Sans MS", 10))
    te1.grid(row = 3, column = 0, sticky = "w", pady = 0, padx = 20)
    te1.config(cursor = "pirate")
    td1 = Label(frame1, bg = "#ffffff", width = 20 )
    td1.grid(row = 4, column = 0, sticky = "e", pady = 1, padx = 20)
    td1.config(fg = "blue", justify = "center")  

    te1r = Label(frame1, text = "theta1", bg = "#86f1ef", font=("Comic Sans MS", 10))
    te1r.grid(row = 3, column = 1, sticky = "w", pady = 0, padx = 20)
    te1r.config(cursor = "pirate")
    td1r = Label(frame1, bg = "#ffffff", width = 20 )
    td1r.grid(row = 4, column = 1, sticky = "e", pady = 1, padx = 20)
    td1r.config(fg = "blue", justify = "center")

    te2 = Label(frame1, text = "Py", bg = "#86f1ef", font=("Comic Sans MS", 10))
    te2.grid(row = 6, column = 0, sticky = "w", pady = 0, padx = 20)
    te2.config(cursor = "pirate")
    td2 = Label(frame1, bg = "#ffffff", width = 20 )
    td2.grid(row = 7, column = 0, sticky = "e", pady = 1, padx = 20)
    td2.config(fg = "blue", justify = "center")

    te2r = Label(frame1, text = "theta2", bg = "#86f1ef", font=("Comic Sans MS", 10))
    te2r.grid(row = 6, column = 1, sticky = "w", pady = 0, padx = 20)
    te2r.config(cursor = "pirate")
    td2r = Label(frame1, bg = "#ffffff", width = 20 )
    td2r.grid(row = 7, column = 1, sticky = "e", pady = 1, padx = 20)
    td2r.config(fg = "blue", justify = "center")

    te3 = Label(frame1, text = "Pz", bg = "#86f1ef", font=("Comic Sans MS", 10))
    te3.grid(row = 9, column = 0, sticky = "w", pady = 0, padx = 20)
    te3.config(cursor = "pirate")
    td3 = Label(frame1, bg = "#ffffff", width = 20 )
    td3.grid(row = 10, column = 0, sticky = "e", pady = 1, padx = 20)
    td3.config(fg = "blue", justify = "center")

    te3r = Label(frame1, text = "tetha3", bg = "#86f1ef", font=("Comic Sans MS", 10))
    te3r.grid(row = 9, column = 1, sticky = "w", pady = 0, padx = 20)
    te3r.config(cursor = "pirate")
    td3r = Label(frame1, bg = "#ffffff", width = 20 )
    td3r.grid(row = 10, column = 1, sticky = "e", pady = 1, padx = 20)
    td3r.config(fg = "blue", justify = "center")
   
    x = 0
    y = 0
    z = -358
    td1["text"] = x
    td2["text"] = y
    td3["text"] = z
    v_falcon = falconPos()
    td1["text"] = v_falcon.X
    td2["text"] = v_falcon.Y
    td3["text"] = v_falcon.Z
    
    
    while not rospy.is_shutdown(): 
        try: 
                vp.update()
		vp.update_idletasks()
        	rate.sleep()
	except:
		break
    rospy.spin()

if __name__ == '__main__':
    publisher()



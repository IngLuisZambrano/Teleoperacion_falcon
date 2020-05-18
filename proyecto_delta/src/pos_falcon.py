#!/usr/bin/env python
# coding: utf-8
import rospy
from ik import *
import numpy as np
import pandas as pd
import tkMessageBox
from Tkinter import *
from dynamixel_sdk import *
from ros_falcon.msg import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

global motor1,motor2, motor3, X, Y, Z, ri, FX, FY, FZ
global datosx, datosy, datosz, c, df, datos, datost
datosx = []
datosy = []
datosz = []
datost = []
c = 0

def callback_function(data):
    global motor1,motor2, motor3, X, Y, Z, ri, FX, FY, FZ
    global datosx, datosy, datosz, datost, c, df, datos
    X = -100+(data.X-(-52))*1.8518
    Y = -150+(data.Y-(-53))*3.173
    Z = -400 + (data.Z-(50))*-2.1
    FX = data.X
    FY = data.Y
    FZ = data.Z
    posicion = falconPos()
    ri = inverse(X, Y, Z)
    motor1 = int(round(3800 - 10.8888*ri[0]))
    motor2 = int(round(3050 - 11.8888*ri[1]))
    motor3 = int(round(2350 - 11.4444*ri[2]))
    posicion.X = motor1
    posicion.Y = motor2
    posicion.Z = motor3
    #datost.append(rospy.Time.now())
    #datosx.append(X)
    #datosy.append(Y)
    #datosz.append(Z)
    #rospy.Time.now()
    #datos = {'Tiempo': datost, 'Pos_Fx': datosx, 'Pos_Fy': datosy, 'Pos_Fz': datosz}
    
    pub.publish(posicion)
    print X, Y, Z

rospy.init_node('tele_remota', anonymous=True) 
rospy.Subscriber("/falconPos", falconPos, callback_function) 
pub = rospy.Publisher('/ir_pos', falconPos, queue_size= 10) 

vp = Tk()
vp.title("Teleoperación Remota")
vp.geometry("800x480+0+0")
vp.config(relief="sunken", bd=10)
imagen = PhotoImage(file="~/catkin_ws/src/proyecto_delta/src/esc.png")
fondo = Label(vp, image=imagen).place(x=580,y=0)
   
#vp.resizable(0, 0)
# Configuración de Frame1
frame1 = Frame(vp, width = 200, height = 250 )
frame1.pack(side = "left", anchor = "n")
frame1.config(bg="#f9a994", cursor="hand2")

frame2 = Frame(vp, width = 200, height = 250 )
frame2.pack(side = "left", anchor = "n")
frame2.config(bg="#80f669", cursor="hand2")

frame3 = Frame(vp, width = 200, height = 250 )
frame3.pack(side = "left", anchor = "n")
frame3.config(bg="#acb8ef", cursor="hand2")

tc4 = Label(frame1, bg = "#f9a994")
tc4.grid(row = 0, column = 0, padx = 2, pady = 1)
tc58 = Label(frame1, bg = "#f9a994")
tc58.grid(row = 8, column = 0, padx = 2, pady = 1)
tc59 = Label(frame2, bg = "#80f669")
tc59.grid(row = 8, column = 0, padx = 2, pady = 1)


tc3 = Label(frame1, text= "Falcon", bg = "#f9a994", font=("Comic Sans MS", 18))
tc3.grid(row = 1, column = 0, padx = 2, pady = 1)

tc1 = Label(frame2, bg = "#80f669")
tc1.grid(row = 0, column = 2, padx = 2, pady = 1)

tc2 = Label(frame2, text= "Motores", bg = "#80f669", font=("Comic Sans MS", 18))
tc2.grid(row = 1, column = 2, padx = 2, pady = 1)

tc5 = Label(frame3, bg = "#acb8ef")
tc5.grid(row = 0, column = 2, padx = 2, pady = 1)

tc6 = Label(frame3, text= "RPD", bg = "#acb8ef", font=("Comic Sans MS", 18))
tc6.grid(row = 1, column = 2, padx = 2, pady = 1)

# Falcon
te1 = Label(frame1, text = "Px", bg = "#f9a994", font=("Comic Sans MS", 10))
te1.grid(row = 2, column = 0, sticky = "w", pady = 0, padx = 20)
te1.config(cursor = "pirate")
td1 = Label(frame1, bg = "#ffffff", width = 20 )
td1.grid(row = 3, column = 0, sticky = "e", pady = 1, padx = 20)
td1.config(fg = "blue", justify = "center")

te1r = Label(frame2, text = "Motor 1", bg = "#80f669", font=("Comic Sans MS", 10))
te1r.grid(row = 2, column = 1, sticky = "w", pady = 0, padx = 20)
te1r.config(cursor = "pirate")
td1r = Label(frame2, bg = "#ffffff", width = 10 )
td1r.grid(row = 3, column = 1, sticky = "w", pady = 1, padx = 20)
td1r.config(fg = "blue", justify = "center")

te1r2 = Label(frame2, text = "theta1", bg = "#80f669", font=("Comic Sans MS", 10))
te1r2.grid(row = 2, column = 2, sticky = "w", pady = 0, padx = 20)
te1r2.config(cursor = "pirate")
td1r2 = Label(frame2, bg = "#ffffff", width = 10 )
td1r2.grid(row = 3, column = 2, sticky = "w", pady = 1, padx = 20)
td1r2.config(fg = "blue", justify = "center")

te1r2d = Label(frame3, text = "Px", bg = "#acb8ef", font=("Comic Sans MS", 10))
te1r2d.grid(row = 2, column = 2, sticky = "w", pady = 0, padx = 20)
te1r2d.config(cursor = "pirate")
td1r2d = Label(frame3, bg = "#ffffff", width = 10 )
td1r2d.grid(row = 3, column = 2, sticky = "w", pady = 1, padx = 20)
td1r2d.config(fg = "blue", justify = "center")

te2 = Label(frame1, text = "Py", bg = "#f9a994", font=("Comic Sans MS", 10))
te2.grid(row = 4, column = 0, sticky = "w", pady = 0, padx = 20)
te2.config(cursor = "pirate")
td2 = Label(frame1, bg = "#ffffff", width = 20 )
td2.grid(row = 5, column = 0, sticky = "e", pady = 1, padx = 20)
td2.config(fg = "blue", justify = "center")

te2r = Label(frame2, text = "Motor 2", bg = "#80f669", font=("Comic Sans MS", 10))
te2r.grid(row = 4, column = 1, sticky = "w", pady = 0, padx = 20)
te2r.config(cursor = "pirate")
td2r = Label(frame2, bg = "#ffffff", width = 10 )
td2r.grid(row = 5, column = 1, sticky = "w", pady = 1, padx = 20)
td2r.config(fg = "blue", justify = "center")

te2r2 = Label(frame2, text = "theta2", bg = "#80f669", font=("Comic Sans MS", 10))
te2r2.grid(row = 4, column = 2, sticky = "w", pady = 0, padx = 20)
te2r2.config(cursor = "pirate")
td2r2 = Label(frame2, bg = "#ffffff", width = 10 )
td2r2.grid(row = 5, column = 2, sticky = "w", pady = 1, padx = 20)
td2r2.config(fg = "blue", justify = "center")

te2r2d = Label(frame3, text = "Py", bg = "#acb8ef", font=("Comic Sans MS", 10))
te2r2d.grid(row = 4, column = 2, sticky = "w", pady = 0, padx = 20)
te2r2d.config(cursor = "pirate")
td2r2d = Label(frame3, bg = "#ffffff", width = 10 )
td2r2d.grid(row = 5, column = 2, sticky = "w", pady = 1, padx = 20)
td2r2d.config(fg = "blue", justify = "center")

te3 = Label(frame1, text = "Pz", bg = "#f9a994", font=("Comic Sans MS", 10))
te3.grid(row = 6, column = 0, sticky = "w", pady = 0, padx = 20)
te3.config(cursor = "pirate")
td3 = Label(frame1, bg = "#ffffff", width = 20 )
td3.grid(row = 7, column = 0, sticky = "e", pady = 1, padx = 20)
td3.config(fg = "blue", justify = "center")

tc58 = Label(frame1, bg = "#f9a994")
tc58.grid(row = 9, column = 0, padx = 2, pady = 1)

te3r = Label(frame2, text = "Motor 3", bg = "#80f669", font=("Comic Sans MS", 10))
te3r.grid(row = 6, column = 1, sticky = "w", pady = 0, padx = 20)
te3r.config(cursor = "pirate")
td3r = Label(frame2, bg = "#ffffff", width = 10 )
td3r.grid(row = 7, column = 1, sticky = "w", pady = 1, padx = 20)
td3r.config(fg = "blue", justify = "center")

te3r3 = Label(frame2, text = "theta3", bg = "#80f669", font=("Comic Sans MS", 10))
te3r3.grid(row = 6, column = 2, sticky = "w", pady = 0, padx = 20)
te3r3.config(cursor = "pirate")
td3r3 = Label(frame2, bg = "#ffffff", width = 10 )
td3r3.grid(row = 7, column = 2, sticky = "w", pady = 1, padx = 20)
td3r3.config(fg = "blue", justify = "center")

tc59 = Label(frame2, bg = "#80f669")
tc59.grid(row = 9, column = 0, padx = 2, pady = 1)

te3r2d = Label(frame3, text = "Pz", bg = "#acb8ef", font=("Comic Sans MS", 10))
te3r2d.grid(row = 6, column = 2, sticky = "w", pady = 0, padx = 20)
te3r2d.config(cursor = "pirate")
td3r2d = Label(frame3, bg = "#ffffff", width = 10 )
td3r2d.grid(row = 7, column = 2, sticky = "w", pady = 1, padx = 20)
td3r2d.config(fg = "blue", justify = "center")

def codigoboton1():
        s = tkMessageBox.askyesno(message="¿Desea continuar?", title="Título")
        if s == False:
		vp.destroy()

boton1= Button(frame3, text = "Cerrar", command = codigoboton1, bg = "#f92103")
boton1.grid(row = 8, column = 2, pady = 8, padx = 4)

while not rospy.is_shutdown(): 
	try: 	
                #df = pd.DataFrame(datos, columns = ['Tiempo','Pos_Fx','Pos_Fy','Pos_Fz'])
                #df.to_excel('Datosff.xlsx', sheet_name = 'Datos') 
                td1r["text"] = motor1
                td2r["text"] = motor2
                td3r["text"] = motor3
                td1["text"]  = FX
                td2["text"]  = FY
                td3["text"]  = FZ 
                td1r2d["text"]  = int(X)
                td2r2d["text"]  = int(Y)
                td3r2d["text"]  = int(Z)
                td1r2["text"]  = int(ri[0])
                td2r2["text"]  = int(ri[1])
                td3r3["text"]  = int(ri[2])
                vp.update()
		vp.update_idletasks()
        	#rate.sleep()
	except:
		break
rospy.spin()






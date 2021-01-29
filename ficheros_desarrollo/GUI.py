# !/usr/bin/python3
from tkinter import *
from tkinter import messagebox
from mock_funcionalidades import Funcionalidades as func
#cambiar func por pou

root = Tk()
root.geometry("800x600")
"""
def muestraVelocidad():
	pou.velocidad_actual()
   	msg = messagebox.showinfo( "Velocidad", "La velocidad actual es: {} rpm".format(pou.velocidad))

def muestraPosicion():
	pou.posicion_actual()
   	msg = messagebox.showinfo( "Posición", "La posición actual es: {}".format(pou.posicion))
"""
botonEncender = Button(root, text = "Encender", width = 10, command = func.encender)
botonEncender.place(x = 50, y = 50)
botonApagar = Button(root, text = "Apagar", width = 10, command = func.apagar)
botonApagar.place(x = 50, y = 100)
botonResetear = Button(root, text = "Resetear", width = 10, command = func.resetear)
botonResetear.place(x = 50, y = 150)
"""
botonMuestraVelocidad = Button(root, text = "Mostrar Velocidad", width = 20, command = muestraVelocidad)
botonMuestraVelocidad.place(x = 250, y = 75)
botonMuestraPosicion = Button(root, text = "Mostrar Posición", width = 20, command = muestraPosicion)
botonMuestraPosicion.place(x = 250, y = 125)
"""
L1 = Label(root, text = "Velocidad = ")
L1.place(x = 400, y = 50)
E1 = Entry(root, bd = 5)
E1.place(x = 475, y = 50)
vel = E1.get()

L2 = Label(root, text = "Vueltas = ")
L2.place(x = 400, y = 100)
E2 = Entry(root, bd = 5)
E2.place(x = 475, y = 100)
vueltas = E2.get()

L3 = Label(root, text = "Posición = ")
L3.place(x = 400, y = 150)
E3 = Entry(root, bd = 5)
E3.place(x = 475, y = 150)
pos_obj = E3.get()

boton_velCte = Button(root, text = "Mover a velocidad constante", width = 30, command = func.movimiento_cte(vel))
boton_velCte.place(x = 150, y = 50)
boton_moveRel = Button(root, text = "Mover N vueltas", width = 30, command = func.movimiento_relativo(vueltas, vel))
boton_moveRel.place(x = 150, y = 100)
boton_moveAbs = Button(root, text = "Mover a posición objetivo", width = 30, command = func.movimiento_absoluto(pos_obj, vel))
boton_moveAbs.place(x = 150, y = 150)


root.mainloop()

#Hacer clase para juntar en main.py y dejar clase en este script: 
# http://www.java2s.com/Code/Python/GUI-Tk/LayoutTOPCENTERandBOTTOM.htm
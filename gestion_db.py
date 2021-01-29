import sqlite3
from sqlite3 import Error

def sql_establishConnection():
    try:
        con = sqlite3.connect('registro_motor.db')

        return con

    except Error:
        print(Error)


def sql_createTable(con):
    cursorObj = con.cursor()

    cursorObj.execute("CREATE TABLE IF NOT EXISTS MOVIMIENTOS(timestamp float PRIMARY KEY, Modo_de_Operación text, UO_Usuario text, Fecha_y_Hora text)")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS USUARIOS(UO_Usuario integer PRIMARY KEY, Nombre text, Apellidos text, Edad integer)")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS MOV_VELOCIDAD_CTE(timestamp float PRIMARY KEY, Velocidad integer, Posición_inicial integer, Posición_final integer)")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS MOV_N_GRADOS(timestamp float PRIMARY KEY, Velocidad integer, Grados integer, Posición_inicial integer, Posición_final integer)")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS MOV_N_VUELTAS(timestamp float PRIMARY KEY, Velocidad integer, Vueltas integer, Posición_inicial integer, Posición_final integer)")

    con.commit()


def insertaDB_usuario(con, uo, name, apellidos, edad):
	con.execute("INSERT INTO USUARIOS (UO_Usuario,Nombre,Apellidos,Edad) \
	     VALUES (?, ?, ?, ?)", (uo, name, apellidos, edad));
	con.commit()


def insertaDB_velCte(con, timestamp, modo, uo, fecha_y_hora, vel, pos_inicial, pos_final):
	
	con.execute("INSERT INTO MOVIMIENTOS (timestamp, Modo_de_Operación, UO_Usuario, Fecha_y_Hora) \
	     VALUES (?, ?, ?, ?)", (timestamp, modo, uo, fecha_y_hora));
	con.commit()

	con.execute("INSERT INTO MOV_VELOCIDAD_CTE(timestamp, Velocidad, Posición_inicial, Posición_final) \
	     VALUES (?, ?, ?, ?)", (timestamp, vel, pos_inicial, pos_final));
	con.commit()


def insertaDB_Ngrados(con, timestamp, modo, uo, fecha_y_hora, vel, grados, pos_inicial, pos_final):

	con.execute("INSERT INTO MOVIMIENTOS (timestamp, Modo_de_Operación, UO_Usuario, Fecha_y_Hora) \
	     VALUES (?, ?, ?, ?)", (timestamp, modo, uo, fecha_y_hora));
	con.commit()

	con.execute("INSERT INTO MOV_N_GRADOS(timestamp, Velocidad, Grados, Posición_inicial, Posición_final) \
	     VALUES (?, ?, ?, ?, ?)", (timestamp, vel, grados, pos_inicial, pos_final));
	con.commit()


def insertaDB_Nvueltas(con, timestamp, modo, uo, fecha_y_hora, vel, vueltas, pos_inicial, pos_final):
	con.execute("INSERT INTO MOVIMIENTOS (timestamp, Modo_de_Operación, UO_Usuario, Fecha_y_Hora) \
	     VALUES (?, ?, ?, ?)", (timestamp, modo, uo, fecha_y_hora));
	con.commit()

	con.execute("INSERT INTO MOV_N_VUELTAS(timestamp, Velocidad, Vueltas, Posición_inicial, Posición_final) \
	     VALUES (?, ?, ?, ?, ?)", (timestamp, vel, vueltas, pos_inicial, pos_final));
	con.commit()

def visualizaDB(con, which):
	cursor = con.cursor()
	if which == 1:
		cursor.execute("SELECT * from MOVIMIENTOS")
		table = cursor.fetchall()
		con.commit()
		print("MOVIMIENTOS")
		for row in table:
			print("Timestamp: ", row[0],"\t | Modo de Operación: ", row[1], "\t | UO Usuario: ", row[2], "\t | Fecha y Hora: ", row[3]) 
	if which == 2:
		cursor.execute("SELECT * from USUARIOS")
		table = cursor.fetchall()
		con.commit()
		print("USUARIOS")
		for row in table:
			print("UO Usuario: ", row[0],"\t | Nombre: ", row[1], "\t | Apellidos: ", row[2], "\t | Edad: ", row[3]) 
	print("\n\n")

			



"""
def identifica_usuario(con, uo):
	cursor = con.cursor()
	cursor.execute("SELECT * from USUARIOS WHERE UO_Usuario = VALUES (?)", (uo))
	usuario = cursor.fetchall()
"""

"""Navegar por DB
cursor = con.cursor()
cursor.execute("SELECT * from MOVIMIENTOS WHERE Modo_de_Operación = 'Velocidad_Cte'")
velocidad_Cte = cursor.fetchall()
print(velocidad_Cte)
timestamp = velocidad_Cte[0]
con.commit()
"""


#para obtener timestamp:
"""
import time
ts = time.gmtime()
timestamp = time.strftime("%s", ts)) #formato UNIX timestamp
fecha_y_hora = time.strftime("%Y-%m-%d %H:%M:%S", ts) #formato fechayhora
"""
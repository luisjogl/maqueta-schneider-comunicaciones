from opcua import Client
from opcua import ua
import time
from POU import POU
from menu import *
import sqlite3
from sqlite3 import Error
from gestion_db import *


if __name__ == '__main__':
    client = Client("opc.tcp://10.0.0.51:4840")
    con = sql_establishConnection()
    
    try:
        print("Conectando")
        client.connect()                                         # conecta el objeto cliente
        root = client.get_root_node()                             # navegacion a traves del arbol de objetos
        objects = root.get_child(['0:Objects'])
        m241 = objects.get_child(['2:M241-M251 data'])
        pou = POU(m241)

        sql_createTable(con)
        
        uo = menu_usuario(con)
        menu_principal(pou, con, uo)

    finally:
        print("Desconectando")
        pou.apagar()
        client.disconnect()
        con.close()

from opcua import Client
from opcua import ua
import time
from POU import POU
from menu import *


if __name__ == '__main__':
    client = Client("opc.tcp://10.0.0.51:4840")
    try:
        print("Conectando")
        client.connect()                                         # conecta el objeto cliente
        root = client.get_root_node()                             # navegacion a traves del arbol de objetos
        objects = root.get_child(['0:Objects'])
        m241 = objects.get_child(['2:M241-M251 data'])
        pou = POU(m241)
        menu_principal(pou)    
    finally:
        print("Desconectando")
        client.disconnect()

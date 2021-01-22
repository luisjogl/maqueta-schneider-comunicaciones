from opcua import Client
from opcua import ua
import time
import sys
sys.path.append("D:\MAIIND\Comunicaciones industriales\maqueta-schneider-comunicaciones-unit-tests-modulos\\")
from modulos_LXM import *
#client = Client("opc.tcp://10.0.0.51:4840")# construye un objeto cliente OPC UA para un servidor
controller = M241()
try:
    print("Conectando")
    
    #client.connect()                                         # conecta el objeto cliente
    #root = client.get_root_node()                             # navegaci�n a trav�s del �rbol de objetos
    #objects = root.get_child(['0:Objects'])
    #m241=objects.get_child(['2:M241-M251 data'])
    power_module = MC_Power_LXM()
    power_module.get_enable()
    time.sleep(0.5)
    power_module.set_enable(True)
    time.sleep(3)
    power_module.get_enable()
    power_module.set_enable(False)
    power_module.get_enable()
    
finally:
    print("Desconectando")
    #client.disconnect()
    #controller.client.disconnect()
    del controller

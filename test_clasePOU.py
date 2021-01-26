from opcua import Client
from opcua import ua
import time
from POU import POU

client = Client("opc.tcp://10.0.0.51:4840")              # construye un objeto cliente OPC UA para un servidor
try:
	print("Conectando")
	client.connect()                                         # conecta el objeto cliente
	root = client.get_root_node()                             # navegacion a traves del arbol de objetos
	objects = root.get_child(['0:Objects'])
	m241 = objects.get_child(['2:M241-M251 data'])
	pou = POU(m241)
	#pou.encender()
	#print(pou.enable_power.get_value())
	time.sleep(1)
	#pou.apagar()
	pou.posicion_actual()
	pou.velocidad_actual()

	#pou.movimiento_cte(200)
	#pou.movimiento_relativo(1, 200)

	time.sleep(1)

	pou.posicion_actual()
	pou.velocidad_actual()

	#pou.parar()
	pou.resetear()

finally:
    print("Desconectando")
    client.disconnect()


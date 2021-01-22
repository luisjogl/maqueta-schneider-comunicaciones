from opcua import Client
from opcua import ua
import time

client = Client("opc.tcp://10.0.0.51:4840")              # construye un objeto cliente OPC UA para un servidor
try:
    print("Conectando")
    client.connect()                                         # conecta el objeto cliente
    root = client.get_root_node()                             # navegaci�n a trav�s del �rbol de objetos
    objects = root.get_child(['0:Objects'])
    m241=objects.get_child(['2:M241-M251 data'])
    enable_reset=m241.get_child(['2:POU.IN2'])
    enable_power=m241.get_child(['2:POU.IN0'])
    move=m241.get_child(['2:POU.IN1'])
    #bombilla=m241.get_child(['2:Programa.Bombilla (%QX0.0)'])
    print("Leyendo valor de Enable RESET")                      # lectura de variable del aut�mata
    print(enable_reset.get_value())

    print("Leyendo valor de Enable POWER")
    print(enable_power.get_value())

    print("Leyendo valor de move")
    print(move.get_value())

    dv_true = ua.DataValue(ua.Variant(True,ua.VariantType.Boolean))
    dv_false = ua.DataValue(ua.Variant(False,ua.VariantType.Boolean))

    print("Poniendo valor de Enable RESET a True")
    enable_reset.set_value(dv_true)
    print("Enable RESET?")
    print(enable_reset.get_value())
    print("Poniendo valor de Enable RESET a False")
    enable_reset.set_value(dv_false)
    print("Enable RESET?")
    print(enable_reset.get_value())

    print("Poniendo valor de Enable POWER a True")
    enable_power.set_value(dv_true)

    print("Enable POWER?")
    print(enable_power.get_value())
    time.sleep(3)


    print("Haciendo moverse al motor")
    move.set_value(dv_true)
    print("Motor moviendose?")
    print(move.get_value())
    time.sleep(3)
    #var.set_value(dv)                                  # escritura en variable del aut�mata

finally:
    print("Desconectando")
    client.disconnect()

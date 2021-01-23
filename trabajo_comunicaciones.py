from opcua import Client
from opcua import ua
import time

def main():
    # Establece conexion y define variables empleadas
    client = Client("opc.tcp://10.0.0.51:4840")              # construye un objeto cliente OPC UA para un servidor
    try:
        print("Conectando")
        client.connect()                                         # conecta el objeto cliente
        root = client.get_root_node()                             # navegacion a traves del arbol de objetos
        objects = root.get_child(['0:Objects'])
        m241 = objects.get_child(['2:M241-M251 data'])
        enable_reset = m241.get_child(['2:POU.Enable_Reset'])
        enable_power = m241.get_child(['2:POU.Enable_Power'])
        execute_moveVel = m241.get_child(['2:POU.Execute_MoveVel'])
        velocity_moveVel = m241.get_child(['2:POU.VEL'])
        execute_stop = m241.get_child(['2:POU.Execute_Stop'])
        set_home = m241.get_child(['2:POU.Set_Home'])
        home_position = m241.get_child(['2:POU.home_position'])
        leePosicion = m241.get_child(['2:POU.leePosicion'])
        leeVelocidad = m241.get_child(['2:POU.leeVelocidad'])
        execute_moveAbs = m241.get_child(['2:POU.moveAbs'])
        execute_moveRel = m241.get_child(['2:POU.moveRel'])
        posicion_objetivo = m241.get_child(['2:POU.posicion_objetivo'])
        velocidad = m241.get_child(['2:POU.velocidad'])
        distancia = m241.get_child(['2:POU.distancia'])

        menu()

    finally:
        print("Desconectando")
        client.disconnect()


if __name__ == '__main__':
    main()

#!usr/bin...blablabla

# Aqui van los imports a todos los programas ficheros necesarios y a las
# librerias opcua, time y demás que se necesiten




# Aqui va el menu con llamadas a todas las funciones de modos_de_operacion
def menu():



# Aqui va definida la funcion main()
def main():
    # Establece conexion y define variables empleadas
    client = Client("opc.tcp://10.0.0.51:4840")              # construye un objeto cliente OPC UA para un servidor
    try:
        print("Conectando")
        client.connect()                                         # conecta el objeto cliente
        root = client.get_root_node()                             # navegacion a traves del arbol de objetos
        objects = root.get_child(['0:Objects'])
        m241 = objects.get_child(['2:M241-M251 data'])
        enable_reset = m241.get_child(['2:POU.IN2'])
        enable_power = m241.get_child(['2:POU.IN0'])
        execute_move = m241.get_child(['2:POU.IN1'])
        velocity_move = m241.get_child(['2:POU.VEL'])
        execute_stop =
        menu()

    finally:
        print("Desconectando")
        client.disconnect()


if __name__ == '__main__':
    main()

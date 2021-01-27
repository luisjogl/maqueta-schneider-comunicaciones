def mensajes_menuPrincipal():
    print("Escriba el número correspondiente a la operación que desea realizar y pulse RETURN \n")
    print("1) Encender motor ")
    print("2) Apagar motor ")
    print("3) Resetear ")
    print("4) Mover motor ")
    print("5) Salir de la aplicación \n")

def mensajes_menuMotor():
    print("Seleccione modo de movimiento que desea para el motor: ")
    print("1) Mover a velocidad constante ")
    print("2) Mover N vueltas")
    print("3) Mover N grados")
    print("4) Volver al menú principal \n")

def menu_motor(pou):
    mensajes_menuMotor()
    seleccion = int(input())
    while seleccion != 4:
        if seleccion == 1:
            print("Por favor, introduzca velocidad a la que desea moverse en rpm: ")
            vel = int(input())
            pou.movimiento_cte(vel)
            print("Para parar el motor y volver a selección de modo pulse 0 y RETURN cuando lo desee.")
            opcion = int(input())
            if opcion == 0:
                pou.parar()
                pass                
            else:
                print("Selección inválida, pulse 0 y RETURN para parar el motor")
        elif seleccion == 2:
            print("Por favor, introduzca velocidad a la que desea moverse en rpm: ")
            vel = int(input())
            print("Por favor, introduzca número de vueltas que desea moverse: ")
            vueltas = int(input())
            pou.movimiento_relativo(vueltas, vel, 0)
            print("Para parar el motor y volver a selección de modo pulse 0 y RETURN cuando lo desee.")
            opcion = int(input())
            if opcion == 0:
                pou.parar()
                pass
            else:
                print("Selección inválida, pulse 0 y RETURN para parar el motor")
        elif seleccion == 3:
            print("Por favor, introduzca velocidad a la que desea moverse en rpm: ")
            vel = int(input())
            print("Por favor, introduzca los grados que desea moverse desde la posición actual: " )
            grados = int(input())
            pou.movimiento_relativo(grados, vel, 1)
            print("Para parar el motor y volver a selección de modo pulse 0 y RETURN cuando lo desee.")
            opcion = int(input())
            if opcion == 0:
                pou.parar()
                pass
            else:
                print("Selección inválida, pulse 0 y RETURN para parar el motor")
        else:
            print("Selección inválida, escoja operación de nuevo. \n")    

        mensajes_menuMotor()
        seleccion = int(input())


def menu_principal(pou):
    mensajes_menuPrincipal()
    seleccion = int(input())

    while seleccion != 5:
        if seleccion == 1:
            pou.encender()
        elif seleccion == 2:
            pou.apagar()
        elif seleccion == 3:
            pou.resetear()
        elif seleccion == 4:
            menu_motor(pou)
        else:
            print("Selección inválida, escoja operación de nuevo. \n")

        mensajes_menuPrincipal()
        seleccion = int(input("Seleccione operación a realizar: \n"))

    print("Ha decidido salir de la aplicación. Adiós! \n")

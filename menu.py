def mensajes_menuPrincipal():
    print("Escriba el número correspondiente a la operación que desea realizar y pulse RETURN \n")
    print("1) Encender motor ")
    print("2) Apagar motor ")
    print("3) Resetear ")
    print("4) Mover motor ")
    print("5) Salir de la aplicación \n")


def menu_principal():
    mensajes_menuPrincipal()
    seleccion = int(input())

    while seleccion != 5:
        if seleccion == 1:
            pou.encender()
        elif seleccion == 2:
            pou.apagar()
        else:
            print("Selección inválida, escoja operación de nuevo. \n")

        mensajes_menuPrincipal()
        seleccion = int(input("Seleccione operación a realizar: \n"))

    print("Ha decidido salir de la aplicación. Adiós! \n")

def menu():

    #mensajes_pantalla()
    seleccion = int(raw_input("Seleccione operación a realizar: \n"))

    while seleccion != 0:
        if seleccion == 1:
            #llamada a seleccion1
        elif seleccion == 2:
            #llamada a seleccion2
        else:
            print("Selección inválida, escoja operación de nuevo. \n")

        #mensajes_pantalla()
        seleccion = int(raw_input("Seleccione operación a realizar: \n"))

    print("Ha decidido salir de la aplicación. Adiós! \n")

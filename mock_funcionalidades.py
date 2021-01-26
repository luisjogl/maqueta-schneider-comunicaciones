import time

class Funcionalidades():

    def encender():
        print("encendiendo")

    def apagar():
        print("apagando")

    def posicion_actual():
        print("la posicion actual es: ___")

    def velocidad_actual():
        print("la velocidad actual es: ___")

    def movimiento_cte(vel): #mover a velocidad constante
        print("mover a velocidad constante, vel: {}".format(vel))

    def movimiento_relativo(vueltas, vel):
        print("me estoy moviendo {} vueltas a {} revoluciones por minuto".format(vueltas, vel))
    
    def movimiento_absoluto(pos_obj, vel): #mover hasta pos elegida(posicion_objetivo) a una velocidad
        print("me estoy moviendo a la posicion {} a una velocidad de {} revoluciones por minuto".format(pos_obj, vel))

    def parar():
        print("parando el motor")

    def resetear():
        print("reseteando, solucionando problemas")

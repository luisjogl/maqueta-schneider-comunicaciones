from opcua import Client
from opcua import ua
import time

def encender():
    try:
        if enable_power.get_value() != dv_BOOL(True): #hay que comprobar si es dv_BOOL(False) o directamente False
            enable_power.set_value(dv_BOOL(True))
            leePosicion.set_value(dv_BOOL(True))
            leeVelocidad.set_value(dv_BOOL(True))
        else:
            pass
    except error_Power.get_value() == dv_BOOL(True): #hay que comprobar si es dv_BOOL(False) o directamente False
        execute_reset.set_value(dv_BOOL(True))
        time.sleep(0.5)
        execute_reset.set_value(dv_BOOL(False))
        enable_power.set_value(dv_BOOL(True))
        leePosicion.set_value(dv_BOOL(True))
        leeVelocidad.set_value(dv_BOOL(True))

def apagar():
    try:
        if enable_power.get_value() != dv_BOOL(False): #hay que comprobar si es dv_BOOL(False) o directamente False
            enable_power.set_value(dv_BOOL(False))
            leePosicion.set_value(dv_BOOL(False))
            leeVelocidad.set_value(dv_BOOL(False))
        else:
            pass
    except error_Power.get_value() == dv_BOOL(True): #hay que comprobar si es dv_BOOL(False) o directamente False
        execute_reset.set_value(dv_BOOL(True))
        time.sleep(0.5)
        execute_reset.set_value(dv_BOOL(False))
        enable_power.set_value(dv_BOOL(False))
        leePosicion.set_value(dv_BOOL(False))
        leeVelocidad.set_value(dv_BOOL(False))

#solo añadir get_value en estas, se usan para base de datos y en cualquiera de los modos de funcionamiento
def posicion_actual():
    if leePosicion.get_value() != dv_BOOL(False): #hay que comprobar si es dv_BOOL(False) o directamente False
        posicion = posicionActual.get_value()
        print(posicion / 16384)
        #añadir return y crear popup que lo muestre en HMI
    else:
        leePosicion.set_value(dv_BOOL(True))
        posicion = posicionActual.get_value()
        print(posicion / 16384)
        #añadir return y crear popup que lo muestre en HMI

def velocidad_actual():
    if leeVelocidad.get_value() != dv_BOOL(False): #hay que comprobar si es dv_BOOL(False) o directamente False
        velocidad = velocidadActual.get_value()
        print(velocidad)
        #añadir return y crear popup que lo muestre en HMI
    else:
        leeVelocidad.set_value(dv_BOOL(True))
        velocidad = velocidadActual.get_value()
        print(velocidad)
        #añadir return y crear popup que lo muestre en HMI

def movimiento_cte(vel): #mover a velocidad constante
    try:
        velocity_moveVel.set_value(dv_DINT(vel))
        execute_moveVel.set_value(dv_BOOL(True))

    except error_MoveVel.get_value() == dv_BOOL(True): #hay que comprobar si es dv_BOOL(False) o directamente False
        execute_reset.set_value(dv_BOOL(True))
        time.sleep(0.5)
        execute_reset.set_value(dv_BOOL(False))
        velocity_moveVel.set_value(dv_DINT(vel))
        execute_moveVel.set_value(dv_BOOL(True))

def movimiento_relativo(vueltas, vel):
    dist = vueltas * 16384 # 1 vuelta = 16384
    try:
        distancia.set_value(dv_DINT(dist))
        velocidad.set_value(dv_DINT(vel))
        execute_moveRel.set_value(dv_BOOL(True))

    except error_moveRelativo.get_value() == dv_BOOL(True): #hay que comprobar si es dv_BOOL(False) o directamente False
        execute_reset.set_value(dv_BOOL(True))
        time.sleep(0.5)
        execute_reset.set_value(dv_BOOL(False))
        distancia.set_value(dv_DINT(dist))
        velocidad.set_value(dv_DINT(vel))
        execute_moveRel.set_value(dv_BOOL(True))

def movimiento_absoluto(pos_obj, vel): #mover hasta pos elegida(posicion_objetivo) a una velocidad
    try:
        posicion_objetivo.set_value(dv_DINT(pos_obj))
        velocidad.set_value(dv_DINT(vel))
        execute_moveAbs.set_value(dv_BOOL(True))

    except error_moveAbsolute.get_value() == dv_BOOL(True): #hay que comprobar si es dv_BOOL(False) o directamente False
        execute_reset.set_value(dv_BOOL(True))
        time.sleep(0.5)
        execute_reset.set_value(dv_BOOL(False))
        posicion_objetivo.set_value(dv_DINT(pos_obj))
        velocidad.set_value(dv_DINT(vel))
        execute_moveAbs.set_value(dv_BOOL(True))

def parar():
    try:
        execute_stop.set_value(dv_BOOL(True))

    except error_Stop.get_value() == dv_BOOL(True): #hay que comprobar si es dv_BOOL(False) o directamente False
        execute_reset.set_value(dv_BOOL(True))
        time.sleep(0.5)
        execute_reset.set_value(dv_BOOL(False))
        execute_stop.set_value(dv_BOOL(True))

def resetear():
    try:
        execute_reset.set_value(dv_BOOL(True))
        time.sleep(0.5)
        execute_reset.set_value(dv_BOOL(False))

    except error_Reset.get_value() == dv_BOOL(True):
        print("Ha habido un error al resetear")

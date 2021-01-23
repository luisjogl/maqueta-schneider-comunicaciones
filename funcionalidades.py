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
    except error_Power == dv_BOOL(True):
        execute_reset.set_value(dv_BOOL(True))
        time.sleep(0.5)
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
    except error_Power == dv_BOOL(True):
        execute_reset.set_value(dv_BOOL(True))
        time.sleep(0.5)
        enable_power.set_value(dv_BOOL(False))
        leePosicion.set_value(dv_BOOL(False))
        leeVelocidad.set_value(dv_BOOL(False))

#def resetear():
def set_home():

#opciones menu
def mover_a(velocidad): #mover cte
def movimiento_relativo(): #mover relativo desde pos actual o desde pos escogida (set_home)
def movimiento_absoluto(): #mover hasta pos elegida(posicion_objetivo) a una velocidad
def parar(): #en cualquier momento

#solo añadir get_value en estas, se usan para base de datos y en cualquiera de los modos de funcionamiento
def posicion_actual():
def velocidad_actual():

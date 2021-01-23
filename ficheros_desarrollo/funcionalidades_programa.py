from opcua import Client
from opcua import ua
import time
import sys
sys.path.append("D:\MAIIND\Comunicaciones industriales\maqueta-schneider-comunicaciones-unit-tests-modulos\\")
from modulos_LXM import *

def encender():
    power_module = MC_Power_LXM()
    time.sleep(0.5)
    power_module.set_enable(True)
    time.sleep(0.5)
    if power_module.get_enable()==True:
        print("El Servo Motor se encendió correctamente\n")
    else:
        print("No se ha podido encender el Servo Motor\n")
    del power_module

def apagar():
    power_module = MC_Power_LXM()
    time.sleep(0.5)
    power_module.set_enable(False)
    time.sleep(0.5)
    if power_module.get_enable()==False:
        print("El Servo Motor se apagó correctamente\n")
    else:
        print("No se ha podido encender el Servo Motor\n")
    del power_module

def resetear():
    reset_module = MC_Reset_LXM()
    time.sleep(0.5)
    reset_module.set_enable(True)
    time.sleep(0.5)
    if reset_module.get_enable()==True:
        print("Reseteado\n")
    else:
        print("No se ha podido resetear\n")
    del reset_module

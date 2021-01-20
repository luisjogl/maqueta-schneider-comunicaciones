from opcua import Client
from opcua import ua
import time


def resetear():
    enable_reset=m241.get_child(['2:POU.IN2'])
    enable_power.set_value(dv_true)
    time.sleep(0.5)
    enable_reset.set_value(dv_false)

def arrancar():
    enable_power=m241.get_child(['2:POU.IN0'])
    if enable_power.get_value() == dv_false:
        enable_power.set_value(dv_true)
    else:
        print("El motor ya está arrancado")

def mover_motor(velocidad):
    move=m241.get_child(['2:POU.IN1'])
    set_vel
    ua.DataValue(ua.Variant([velocidad], ua.VariantType.Int64))

def parar_motor():
    stop_motor = m241.get_child(['2:POU.IN3'])
    stop_motor.set_value(dv_true)
    time.sleep(0.5)
    stop_motor.set_value(dv_false)

def set_home_position():
    set_home=m241.get_child(['2:POU.homing'])

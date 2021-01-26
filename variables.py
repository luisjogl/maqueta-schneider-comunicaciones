from opcua import Client
from opcua import ua
import time

class Variables():
    def __init__(self, controller):
        self.execute_reset = controller.get_child(['2:POU.Execute_Reset'])
        self.enable_power = controller.get_child(['2:POU.Enable_Power'])
        self.execute_moveVel = controller.get_child(['2:POU.Execute_MoveVel'])
        self.velocity_moveVel = controller.get_child(['2:POU.VEL'])
        self.execute_stop = controller.get_child(['2:POU.Execute_Stop'])
        self.set_home = controller.get_child(['2:POU.Set_Home'])
        self.home_position = controller.get_child(['2:POU.home_position'])
        self.leePosicion = controller.get_child(['2:POU.leePosicion'])
        self.leeVelocidad = controller.get_child(['2:POU.leeVelocidad'])
        self.posicionActual = controller.get_child(['2:POU.posicionActual'])
        self.velocidadActual = controller.get_child(['2:POU.velocidadActual'])
        self.execute_moveAbs = controller.get_child(['2:POU.moveAbs'])
        self.execute_moveRel = controller.get_child(['2:POU.moveRel'])
        self.posicion_objetivo = controller.get_child(['2:POU.posicion_objetivo'])
        self.velocidad = controller.get_child(['2:POU.velocidad'])
        self.distancia = controller.get_child(['2:POU.distancia'])
        self.error_Power = controller.get_child(['2:POU.error_Power'])
        self.error_MoveVel = controller.get_child(['2:POU.error_MoveVel'])
        self.error_Reset = controller.get_child(['2:POU.error_Reset'])
        self.error_Stop = controller.get_child(['2:POU.error_Stop'])
        self.error_setHome = controller.get_child(['2:POU.error_setHome'])
        self.error_moveRelativo = controller.get_child(['2:POU.error_moveRelativo'])
        self.error_moveAbsoluto = controller.get_child(['2:POU.error_moveAbsolute'])
        
    def dv_BOOL(self, bool_value):
        return ua.DataValue(ua.Variant(bool_value,ua.VariantType.Boolean))

    def dv_DINT(self, value):
        return ua.DataValue(ua.Variant([value], ua.VariantType.Int32))

    def encender(self):
        try:
            if self.enable_power.get_value() != self.dv_BOOL(True): #hay que comprobar si es dv_BOOL(False) o directamente False
                self.enable_power.set_value(self.dv_BOOL(True))
                self.leePosicion.set_value(self.dv_BOOL(True))
                self.leeVelocidad.set_value(self.dv_BOOL(True))
            else:
                pass
        except self.error_Power.get_value() == self.dv_BOOL(True): #hay que comprobar si es dv_BOOL(False) o directamente False
            self.execute_reset.set_value(self.dv_BOOL(True))
            time.sleep(0.5)
            self.execute_reset.set_value(self.dv_BOOL(False))
            self.enable_power.set_value(self.dv_BOOL(True))
            self.leePosicion.set_value(self.dv_BOOL(True))
            self.leeVelocidad.set_value(self.dv_BOOL(True))
    
    def apagar(self):
        try:
            if self.enable_power.get_value() != self.dv_BOOL(False): #hay que comprobar si es dv_BOOL(False) o directamente False
                self.enable_power.set_value(self.dv_BOOL(False))
                self.leePosicion.set_value(self.dv_BOOL(False))
                self.leeVelocidad.set_value(self.dv_BOOL(False))
            else:
                pass
        except self.error_Power.get_value() == self.dv_BOOL(True): #hay que comprobar si es dv_BOOL(False) o directamente False
            self.execute_reset.set_value(self.dv_BOOL(True))
            time.sleep(0.5)
            self.execute_reset.set_value(self.dv_BOOL(False))
            self.enable_power.set_value(self.dv_BOOL(False))
            self.leePosicion.set_value(self.dv_BOOL(False))
            self.leeVelocidad.set_value(self.dv_BOOL(False))    


"""
global enable_power
global execute_reset
global execute_moveVel
global velocity_moveVel
global execute_stop
global set_home
global home_position
global leePosicion
global posicionActual
global velocidadActual
global execute_moveAbs
global execute_moveRel
global posicion_objetivo
global velocidad
global distancia
global error_Power
global error_MoveVel
global error_Reset
global error_Stop
global error_setHome
global error_moveRelativo
global error_moveAbsoluto


def dv_BOOL(bool_value):
    return ua.DataValue(ua.Variant(bool_value,ua.VariantType.Boolean))

def dv_DINT(value):
    return ua.DataValue(ua.Variant([value], ua.VariantType.Int32))

def get_POU_variables(controller):
    execute_reset = controller.get_child(['2:POU.Execute_Reset'])
    enable_power = controller.get_child(['2:POU.Enable_Power'])
    execute_moveVel = controller.get_child(['2:POU.Execute_MoveVel'])
    velocity_moveVel = controller.get_child(['2:POU.VEL'])
    execute_stop = controller.get_child(['2:POU.Execute_Stop'])
    set_home = controller.get_child(['2:POU.Set_Home'])
    home_position = controller.get_child(['2:POU.home_position'])
    leePosicion = controller.get_child(['2:POU.leePosicion'])
    leeVelocidad = controller.get_child(['2:POU.leeVelocidad'])
    posicionActual = controller.get_child(['2:POU.posicionActual'])
    velocidadActual = controller.get_child(['2:POU.velocidadActual'])
    execute_moveAbs = controller.get_child(['2:POU.moveAbs'])
    execute_moveRel = controller.get_child(['2:POU.moveRel'])
    posicion_objetivo = controller.get_child(['2:POU.posicion_objetivo'])
    velocidad = controller.get_child(['2:POU.velocidad'])
    distancia = controller.get_child(['2:POU.distancia'])
    error_Power = controller.get_child(['2:POU.error_Power'])
    error_MoveVel = controller.get_child(['2:POU.error_MoveVel'])
    error_Reset = controller.get_child(['2:POU.error_Reset'])
    error_Stop = controller.get_child(['2:POU.error_Stop'])
    error_setHome = controller.get_child(['2:POU.error_setHome'])
    error_moveRelativo = controller.get_child(['2:POU.error_moveRelativo'])
    error_moveAbsoluto = controller.get_child(['2:POU.error_moveAbsolute'])
"""
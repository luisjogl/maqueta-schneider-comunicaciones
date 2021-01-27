from opcua import Client
from opcua import ua
import time

class POU():
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
        self.doneRel = controller.get_child(['2:POU.doneRel'])
        self.doneAbs = controller.get_child(['2:POU.doneAbs'])

    def dv_BOOL(self, bool_value):
        return ua.DataValue(ua.Variant(bool_value,ua.VariantType.Boolean))

    def dv_DINT(self, value):
        return ua.DataValue(ua.Variant(value, ua.VariantType.Int32))

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

    def posicion_actual(self):
        if self.leePosicion.get_value() != self.dv_BOOL(False): #hay que comprobar si es dv_BOOL(False) o directamente False
            self.posicion = self.posicionActual.get_value()
            print("La posición actual es {}".format(self.posicion))
            return self.posicion
            #añadir return y crear popup que lo muestre en HMI
        else:
            self.leePosicion.set_value(self.dv_BOOL(True))
            self.posicion = self.posicionActual.get_value()
            print("La posición actual es {}".format(self.posicion))
            return self.posicion

    def velocidad_actual(self):
        if self.leeVelocidad.get_value() != self.dv_BOOL(False): #hay que comprobar si es dv_BOOL(False) o directamente False
            self.velocidad = self.velocidadActual.get_value()
            return self.velocidad
            #añadir return y crear popup que lo muestre en HMI
        else:
            self.leeVelocidad.set_value(self.dv_BOOL(True))
            self.velocidad = self.velocidadActual.get_value()
            return self.velocidad
            #añadir return y crear popup que lo muestre en HMI

    def movimiento_cte(self, vel): #mover a velocidad constante
        try:
            self.velocity_moveVel.set_value(self.dv_DINT(vel))
            self.execute_moveVel.set_value(self.dv_BOOL(True))

        except self.error_MoveVel.get_value() == self.dv_BOOL(True): #hay que comprobar si es dv_BOOL(False) o directamente False
            self.execute_reset.set_value(self.dv_BOOL(True))
            time.sleep(0.5)
            self.execute_reset.set_value(self.dv_BOOL(False))
            self.velocity_moveVel.set_value(self.dv_DINT(vel))
            self.execute_moveVel.set_value(self.dv_BOOL(True))

    def movimiento_relativo(self, obj, vel, modo):
        if modo == 0:
            dist = int(obj * 16384) # 1 vuelta = 16384
        else:
            dist = int(obj / 360 * 16384)
        try:
            self.distancia.set_value(self.dv_DINT(dist))
            self.velocidad.set_value(self.dv_DINT(vel))
            #self.velocidad.set_value(self.dv_DINT(vel))
            self.execute_moveRel.set_value(self.dv_BOOL(True))
            time.sleep(0.5)

        except self.error_moveRelativo.get_value() == self.dv_BOOL(True): #hay que comprobar si es dv_BOOL(False) o directamente False
            self.execute_moveRel.set_value(self.dv_BOOL(False))
            self.execute_reset.set_value(self.dv_BOOL(True))
            time.sleep(0.5)
            self.execute_reset.set_value(self.dv_BOOL(False))
            self.distancia.set_value(self.dv_DINT(dist))
            self.velocidad.set_value(self.dv_DINT(vel))
            self.execute_moveRel.set_value(self.dv_BOOL(True))
            time.sleep(0.5)

    def movimiento_absoluto(self, pos_obj, vel): #mover hasta pos elegida(posicion_objetivo) a una velocidad
        try:
            self.posicion_objetivo.set_value(self.dv_DINT(int(pos_obj)))
            self.velocidad.set_value(self.dv_DINT(vel))
            self.execute_moveAbs.set_value(self.dv_BOOL(True))

        except self.error_moveAbsolute.get_value() == self.dv_BOOL(True): #hay que comprobar si es dv_BOOL(False) o directamente False
            self.execute_reset.set_value(self.dv_BOOL(True))
            time.sleep(0.5)
            self.execute_reset.set_value(self.dv_BOOL(False))
            self.posicion_objetivo.set_value(self.dv_DINT(pos_obj))
            self.velocidad.set_value(self.dv_DINT(vel))
            self.execute_moveAbs.set_value(dv_BOOL(True))

    def parar(self):
        try:
            self.execute_stop.set_value(self.dv_BOOL(True))
            self.execute_moveVel.set_value(self.dv_BOOL(False))
            self.execute_moveAbs.set_value(self.dv_BOOL(False))
            self.execute_moveRel.set_value(self.dv_BOOL(False))
            time.sleep(0.5)
            self.execute_stop.set_value(self.dv_BOOL(False))

        except self.error_Stop.get_value() == self.dv_BOOL(True): #hay que comprobar si es dv_BOOL(False) o directamente False
            self.execute_reset.set_value(self.dv_BOOL(True))
            time.sleep(0.5)
            self.execute_reset.set_value(self.dv_BOOL(False))
            self.execute_stop.set_value(self.dv_BOOL(True))
            self.execute_moveVel.set_value(self.dv_BOOL(False))
            self.execute_moveAbs.set_value(self.dv_BOOL(False))
            self.execute_moveRel.set_value(self.dv_BOOL(False))
            time.sleep(0.5)
            self.execute_stop.set_value(self.dv_BOOL(False))

    def resetear(self):
        try:
            self.execute_reset.set_value(self.dv_BOOL(True))
            self.execute_moveVel.set_value(self.dv_BOOL(False))
            self.execute_moveAbs.set_value(self.dv_BOOL(False))
            self.execute_moveRel.set_value(self.dv_BOOL(False))
            time.sleep(0.5)
            self.execute_reset.set_value(self.dv_BOOL(False))

        except self.error_Reset.get_value() == self.dv_BOOL(True):
            print("Ha habido un error al resetear")

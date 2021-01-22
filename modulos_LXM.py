from opcua import Client
from opcua import ua


class M241:
    def __init__(self):
        self.client = Client("opc.tcp://10.0.0.51:4840")
        self.client.connect()                                         # conecta el objeto cliente
        self.root = self.client.get_root_node()                             # navegacion a traves del arbol de objetos
        self.objects = self.root.get_child(['0:Objects'])
        self.m241 = self.objects.get_child(['2:M241-M251 data'])

    def __del__(self):
        self.client.disconnect()

class MC_Power_LXM(M241):
    def __init__(self):
        M241.__init__(self)
        self.enable = self.m241.get_child(['2:POU.IN0'])

    def get_enable(self):
        print(self.enable.get_value())

    def set_enable(self, bool_value):
        self.enable.set_value(ua.DataValue(ua.Variant(bool_value,ua.VariantType.Boolean)))


class MC_Reset_LXM:

    def __init__(self):
        self.execute = m241.get_child(['2:POU.IN2'])

    def get_execute(self):
        execute.get_value()

    def set_execute(self, bool_value):
        execute.set_value(ua.DataValue(ua.Variant(bool_value,ua.VariantType.Boolean)))


class MC_Stop_LXM:

    def __init__(self):
        self.execute = m241.get_child(['2:POU.IN3'])

    def get_execute(self):
        execute.get_value()

    def set_execute(self, bool_value):
        execute.set_value(ua.DataValue(ua.Variant(bool_value,ua.VariantType.Boolean)))


class MC_ReadParameter_LXM:

    def __init__(self):
        self.enable = m241.get_child(['2:POU.leeparam'])
        self.value = m241.get_child(['2:POU.Ana2'])

    def get_enable(self):
        enable.get_value()

    def get_value(self):
        value.get_value()

    def set_enable(self, bool_value):
        execute.set_value(ua.DataValue(ua.Variant(bool_value,ua.VariantType.Boolean)))


class MC_Home_LXM:

    def __init__(self):
        self.execute = m241.get_child(['2:POU.homing'])
        self.position = m241.get_child(['2:POU.home_position']) #TODO:crear variable en SoMachine
        position.set_home_position(0)

    def get_execute(self):
        execute.get_value()

    def set_execute(self, bool_value):
        execute.set_value(ua.DataValue(ua.Variant(bool_value,ua.VariantType.Boolean)))

    def get_home_position(self):
        position.get_value()

    def set_home_position(self, home_position):
        position.set_value(ua.DataValue(ua.Variant([home_position], ua.VariantType.Int32)))


class MC_MoveAbsolute_LXM:

    def __init__(self):
        self.execute = m241.get_child(['2:POU.moveabs'])
        self.position = m241.get_child(['2:POU.target_position']) #TODO:crear variable en SoMachine
        position.set_target_position(0)
        self.velocity = m241.get_child(['2:POU.abs_velocity']) #TODO:crear variable en SoMachine

    def get_execute(self):
        execute.get_value()

    def set_execute(self, bool_value):
        execute.set_value(ua.DataValue(ua.Variant(bool_value,ua.VariantType.Boolean)))

    def get_targetPosition(self):
        position.get_value()

    def set_targetPosition(self, target_position):
        position.set_value(ua.DataValue(ua.Variant([target_position], ua.VariantType.Int32)))

    def get_velocity(self):
        velocity.get_value()

    def set_velocity(self, abs_vel):
        velocity.set_value(ua.DataValue(ua.Variant([abs_vel], ua.VariantType.Int32)))


class MC_MoveRelative_LXM:

    def __init__(self):
        self.execute = m241.get_child(['2:POU.moverel'])
        self.distance = m241.get_child(['2:POU.target_distance']) #TODO:crear variable en SoMachine
        self.velocity = m241.get_child(['2:POU.rel_velocity']) #TODO:crear variable en SoMachine

    def get_execute(self):
        execute.get_value()

    def set_execute(self, bool_value):
        execute.set_value(ua.DataValue(ua.Variant(bool_value,ua.VariantType.Boolean)))

    def get_targetPosition(self):
        position.get_value()

    def set_targetDistance(self, target_distance):
        position.set_value(ua.DataValue(ua.Variant([target_position], ua.VariantType.Int32)))

    def get_velocity(self):
        velocity.get_value()

    def set_velocity(self, rel_vel):
        velocity.set_value(ua.DataValue(ua.Variant([rel_vel], ua.VariantType.Int32)))


#TODO:crear modulo completo en SoMachine
class MC_ReadActualPosition_LXM:
    def __init__(self):
        self.enable = m241.get_child(['2:POU.leeposicion']) #TODO:crear variable en SoMachine
        self.position = m241.get_child(['2:POU.posicionactual']) #TODO:crear variable en SoMachine

    def get_enable(self):
        enable.get_value()

    def set_enable(self, bool_value):
        enable.set_value(ua.DataValue(ua.Variant(bool_value,ua.VariantType.Boolean)))

    def get_actualPosition(self):
        position.get_value()

#TODO:crear modulo completo en SoMachine
class MC_ReadActualVelocity_LXM:
    def __init__(self):
        self.enable = m241.get_child(['2:POU.leeposicion']) #TODO:crear variable en SoMachine
        self.velocity = m241.get_child(['2:POU.velocidadactual']) #TODO:crear variable en SoMachine

    def get_enable(self):
        enable.get_value()

    def set_enable(self, bool_value):
        enable.set_value(ua.DataValue(ua.Variant(bool_value,ua.VariantType.Boolean)))

    def get_actualVelocity(self):
        position.get_value()

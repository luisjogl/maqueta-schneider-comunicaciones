def dv_BOOL(bool_value):
    return ua.DataValue(ua.Variant(bool_value,ua.VariantType.Boolean)))

def dv_DINT(value):
    return ua.DataValue(ua.Variant([value], ua.VariantType.Int32)))

def get_POU_variables(controller):
    global execute_reset = controller.get_child(['2:POU.Execute_Reset'])
    global enable_power = controller.get_child(['2:POU.Enable_Power'])
    global execute_moveVel = controller.get_child(['2:POU.Execute_MoveVel'])
    global velocity_moveVel = controller.get_child(['2:POU.VEL'])
    global execute_stop = controller.get_child(['2:POU.Execute_Stop'])
    global set_home = controller.get_child(['2:POU.Set_Home'])
    global home_position = controller.get_child(['2:POU.home_position'])
    global leePosicion = controller.get_child(['2:POU.leePosicion'])
    global leeVelocidad = controller.get_child(['2:POU.leeVelocidad'])
    global execute_moveAbs = controller.get_child(['2:POU.moveAbs'])
    global execute_moveRel = controller.get_child(['2:POU.moveRel'])
    global posicion_objetivo = controller.get_child(['2:POU.posicion_objetivo'])
    global velocidad = controller.get_child(['2:POU.velocidad'])
    global distancia = controller.get_child(['2:POU.distancia'])
    global error_Power = controller.get_child(['2:POU.error_Power'])
    global error_MoveVel = controller.get_child(['2:POU.error_MoveVel'])
    global error_Reset = controller.get_child(['2:POU.error_Reset'])
    global error_Stop = controller.get_child(['2:POU.error_Stop'])
    global error_setHome = controller.get_child(['2:POU.error_setHome'])

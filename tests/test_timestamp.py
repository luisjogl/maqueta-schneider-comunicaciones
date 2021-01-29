import time
import datetime

time_datetime = datetime.datetime.now()
ts = time.gmtime()
tiempo = time.time()
timestamp = time.strftime("%S", ts) 
fecha_y_hora = time.strftime("%Y-%m-%d %H:%M:%S", ts)     
print(tiempo)
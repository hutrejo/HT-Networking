
#### Aqui se importan las librerias #########

import sys
import time
import os
import cmd
import datetime

######## Nombra el archivo con la fecha y hora actual ##################
now = datetime.datetime.now()
filename = "%.2i%.2i%i_%.2i%.2i%.2i" % (now.year,now.month,now.day,now.hour,now.minute,now.second)

''' Aqui guardas tu listado de ips de las camaras con formato:

192.168.0.1
192.168.0.2
192.168.0.3
.
.
.

NOTA: en un txt y apunta a la carpeta donde esta el txt (MODIFICALO DE ACUERDO A TU DIRECTORIO'''


f0 = open("c:\\Users\\hitg8\\OneDrive\\Documents\\Python\\listaips.txt")

####Es el ciclo para pinguear cada camara#####


for ip in f0.readlines():
    ip = ip.strip()
    response = os.popen(f"ping {ip}").read()
    f1 = open(filename, 'a')
    if "Received = 4" in response:
       f1.write(f"{ip} Ping exitoso, camara UP\n")
    elif "Received = 3" in response:
       f1.write(f"{ip} Ping con 25% de perdidas\n")
    elif "Received = 2" in response:
       f1.write(f"{ip} Ping con 50% de perdidas\n")    
    elif "Received = 1" in response:
       f1.write(f"{ip} Ping con 75% de perdidas\n")
    else:
       f1.write(f"{ip} Camara DOWN\n")

''' Te va a generar un txt cada que lo corras con los mensajes que ves arriba, esto se puede modificar a tu conveniancia, yo puse
pings con perdidas pero si no es el caso puedes dejar solo UP y DOWN, este txt se guarda en la carpeta de donde jalas la lista de camaras ip''' 
           
f0.close()
f1.close()


###No olvides importar paramiko e instalarlo previamente en tu maquina######################
import sys
import paramiko 
import os
import cmd
import time


#######Cambia los valores de acuerdo a tus necesidades, recuerda que los equipos deben tener acceso por remoto por ssh###########
########Debes usar un tftp server que puede ser tu maquina, solo debes usar un software como solar winds, busca en google como convertir
########mi pc en un tftp server########

user = 'hugo'
password = 'hugo'
port=22
ios_new_ver = 'c7200-a3js-mz.122-15.T16.bin'
tftp_server = '10.0.0.96'

##Aqui deben usar el directorio donde esta su txt con la lista de ips de routers a actualizar, no olvides cambiarlo por el tuyo una vez 
###tu maquina sea server
####la lista de ips va en un bloc de notas una ip por linea 
'''
10.10.10.1
20.20.20.20
30.30.30.30
'''
f0 = open("c:\\Users\\hitg8\\OneDrive\\Documents\\Python\\listaips.txt")
for ip in f0.readlines():
       ip = ip.strip()
       #### se conecta por ssh#########################################################################################
       ssh = paramiko.SSHClient()
       ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       ssh.connect(ip,port, user, password, look_for_keys=False)
       chan = ssh.invoke_shell()
       time.sleep(2)
       time.sleep(1)
       ####copia la imagen del server en este casu tu lap o cualquier server que uses a la flash#########################
       chan.send('copy tftp: flash:\n')
       time.sleep(2)
       time.sleep(1)
       chan.send(tftp_server +'\n')
       time.sleep(2)
       time.sleep(1)
       ######la imagen origen###########################################################################################
       chan.send(ios_new_ver +'\n')
       time.sleep(2)
       time.sleep(1)
       ######la imagen destino que es la misma
       chan.send(ios_new_ver +'\n')
       time.sleep(2)
       time.sleep(1)
       #este es un mensaje opcional que borra la flash antes de copiarla Erase flash: before copying? [confirm]n####### 
       # , esto sale en un router cisco 2800###########################################################################
       #puede que por el modelo no lo requiera, si es asi solo comentalo o borralo#####################################
       chan.send('n\n')
       time.sleep(2)
       time.sleep(1)
       #####cambias el registro de configuracion######################################################################
       chan.send('conf t\n')
       time.sleep(1)
       chan.send('config-register 0x2102\n')
       time.sleep(1)
       ######cambias la variable de booteo############################################################################
       chan.send('no boot system\n')
       time.sleep(1)
       chan.send('boot system flash:'+ios_new_ver)
       time.sleep(1)
       chan.send('^Z')
       time.sleep(1)
       #######guardas config y das el reload###########################################################################
       chan.send('write mem'+ios_new_ver)
       time.sleep(1)
       chan.send('reload')
       time.sleep(1)
       chan.send('\n')
       time.sleep(1)
       ssh.close() 
       f0.close()
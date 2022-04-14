import sys
import time
import paramiko 
import os
import cmd
import datetime

now = datetime.datetime.now()
user = 'hugo'
password = 'hugo'

port=22

input_string = input('Ingresa las IPs del los equipos de los cuales deseas obtener logs separados por espacio: ')
print("\n")
user_list = input_string.split()
input_kewword = input('Ingresa la palabra clave con la cual deseas buscar logs: ')
print("\n")

for ip in user_list:
    #print (ip)
    filename_prefix ='/Users/hitg8/Documents/logs/' + ip
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port, user, password, look_for_keys=False)
    chan = ssh.invoke_shell()
    time.sleep(2)
    time.sleep(1)
    chan.send('term len 0\n')
    time.sleep(1)
    chan.send('sh logg' + ' | inc ' + str(input_kewword) + '\n')
    time.sleep(20)
    output = chan.recv(999999)
    filename = "%s_%.2i%.2i%i_%.2i%.2i%.2i" % (ip,now.year,now.month,now.day,now.hour,now.minute,now.second)
    f1 = open(filename, 'a')
    f1.write(output.decode("utf-8") )
    f1.close()
    ssh.close() 
    
    
import os
import datetime
import time
import socket

def salvaArquivo(_tipo, _mensagem):
	arquivo = open("/opt/iot.central/banco/logs.csv","+a")
	arquivo.write('[')
	arquivo.write(datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y %H:%M:%S'))
	arquivo.write('] [')
	arquivo.write(_tipo)
	arquivo.write('] [')
	arquivo.write(_mensagem)
	arquivo.write(']\n')
	arquivo.close()
	print('['+ datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y %H:%M:%S')\
	+ '] [' + _tipo + '] [' + _mensagem + ']')    

"""
Verifica conexão com a Internet
"""

def check_host():
	confiaveis = ['google.com']
	for host in confiaveis:
		a=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		a.settimeout(.5)
		try:
			b=a.connect_ex((host, 80))
			if(b==0): #ok, conectado
				a.close()
				return True
		except:
			a.close()
			return False

	return False
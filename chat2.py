import socket
import threading 
import os
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip = input("\n\t\tEnter Your name : ")
port = 1234
s.bind( (ip,port) )
sip = input("\n\t\tYou want to chat with : ")
sport = 5678
print()
os.system('tput setaf 3')
def send():
    while True:
        os.system('tput setaf 5')
        msg = input('\n').encode()
        s.sendto(msg,(sip,sport))
        if msg.decode() == "exit":
            os._exit(1)
def recv():
    while True:
        os.system('tput setaf 2')
        msg = s.recvfrom(1024)
        if msg[0].decode() == "exit":
            s.sendto("exit".encode(), (sip,sport))
            os._exit(1)
        print('\n\t\t\t\t\t\t\t\t\tReceived -> ' + msg[0].decode())
t1 = threading.Thread(target=send)
t2 = threading.Thread(target=recv)
t1.start()
t2.start()

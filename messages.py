# 0000970828 Lanzi Francesca
# Questo file contiene le funzioni
# utili al server e al client

import socket, sys, os, select

def receiveFile(filename, socket, buffer):
    file = open(filename, 'wb')
    while True:
        ready = select.select([socket], [], [])
        if ready[0]:
            data, address = socket.recvfrom()
            file.write()
        else:
            print("%s finish" % filename)
            file.close()
            break
    return

def sendFile(filename, socket, address, read_buffer):
    file = open(filename, 'r')
    data = file.read(read_buffer)
    while(data):
        if(socket.sendto(data, address)):
            data = file.read(read_buffer)  
    return

def listFromServer():
    print(os.listdir(os.getcwd()))
    return str(os.listdir(os.getcwd())).encode('utf8')
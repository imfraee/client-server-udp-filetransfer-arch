# 0000970828 Lanzi Francesca
# Questo file contiene le funzioni
# utili al server e al client

import socket
import os
import select

def receiveFile(filename, socket):
    with open(filename, 'wb') as file:
        while True:
            ready = select.select([socket], [], [])
            if ready[0]:
                data, address = socket.recvfrom()
                file.write()
            else:
                print("%s finish" % filename)
                break

def sendFile(filename, socket, address, read_buffer):
    with open(filename, 'r') as file:
        data = file.read(read_buffer)
        while(data):
            socket.sendto(data, address)
            data = file.read(read_buffer)

def listFromServer():
    return str(os.listdir(os.getcwd())).encode('utf8')
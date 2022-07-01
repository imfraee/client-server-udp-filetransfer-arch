# 0000970828 Lanzi Francesca
# Questo file contiene le funzioni
# utili al server e al client

import os
import select

def receiveFile(filename, socket, buffer):
    with open(filename, 'wb') as file:
        while True:
            ready = select.select([socket], [], [], 2.0)
            if ready[0]:
                data, address = socket.recvfrom(buffer)
                file.write(data)
            else:
                print("%s finish" % filename)
                break

def sendFile(filename, socket, address, read_buffer):
    with open(filename, 'rb') as file:
        data = file.read(read_buffer)
        while(data):
            socket.sendto(data, address)
            data = file.read(read_buffer)

def listFromServer():
    return str([f for f in os.listdir(os.getcwd()) if os.path.isfile(f)])[1:-1].encode('utf8')
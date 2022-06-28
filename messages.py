# 0000970828 Lanzi Francesca
# Questo file contiene le funzioni
# utili al server e al client

import socket, sys, os

def getFromServer():
    return

def putOnServer(filename, socket):
    file = open(filename, 'rb')
    file_data = file.read(1024)
    socket.send(file_data)
    print("\n\r File sent successufully!")
    return

def getOnServer(filename, socket):
    file = open(filename, 'wb')
    file_data = socket.recv(1024)
    file.write(file_data)
    file.close()
    print("\n\r File received successefully!")
    return

def listFromServer():
    return str(os.listdir(os.getcwd())).encode()
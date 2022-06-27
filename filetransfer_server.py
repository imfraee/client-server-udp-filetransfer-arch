import socket
import time

BUFFSIZE = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('', 10000)
print('\n\r Waiting up on %s, port %s' % server_address)
sock.bind(server_address)

while True:
    print('\n\r Waiting to receive a message... ')
    data, address = sock.recvfrom(BUFFSIZE)
    print('\n\r Received %s bytes from port %s' % (len(data), address))
    print(data.decode('utf8'))
    

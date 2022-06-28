import socket, time
import messages as mes

BUFFSIZE = 4096
PORT = 10000

s_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('', PORT)
print('\n\r Waiting up on %s, port %s' % server_address)
s_sock.bind(server_address)

while True:
    print('\n\r Waiting to receive a message... ')
    data, c_address = s_sock.recvfrom(BUFFSIZE)
    #print('\n\r Received %s bytes from port %s' % (len(data), address))
    line = data.decode('utf8')
    
    if line == 'list':
        s_sock.sendto(mes.listFromServer(), c_address)

    if line == 'exit':
        exit()


import socket, time, sys
sys.path.append('/home/francesca/progetto_reti')
import messages as mes

BUFFSIZE = int(4096)
PORT = int(10000)

s_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', PORT)
print('\n\r Waiting up on %s, port %s' % server_address)
s_sock.bind(server_address)

while True:
    print('\n\r Waiting to receive a message... ')
    data, client = s_sock.recvfrom(BUFFSIZE)
    #print('\n\r Received %s bytes from port %s' % (len(data), address))
    line = data.decode('utf8').split()
    print(data)
    
    if line[0] == 'list':
        s_sock.sendto(mes.listFromServer(), client)
        print("\n\r List sent")

    if line[0] == 'put':
        filename = line[1]
        while True:
            mes.receiveFile(filename, s_sock, BUFFSIZE)
            break
        ok = "\n\rFile received correctly"
        s_sock.sendto(ok.encode('utf8'), server_address)

    if line[0] == 'get':
        filename = line[1]
        s_sock.sendto(filename, server_address)
        print("\n\r Sending %s..." % filename)
        mes.sendFile(filename, s_sock, server_address, BUFFSIZE)

    if line[0] == 'exit':
        exit()


import socket
import sys
import messages as mes

BUFFSIZE = 4096
PORT = 10000

s_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.0', PORT)
print(f'Waiting up on {server_address[0]}, port {server_address[1]}', end = "\n\r")
s_sock.bind(server_address)

try: 
    while True:
        print('Waiting to receive a message...', end="\n\r")
        data, client = s_sock.recvfrom(BUFFSIZE)
        line = data.decode('utf8').split(' ', maxsplit=1)
        print(data)
        
        if line[0] == 'list':
            s_sock.sendto(mes.listFromServer(), client)
            print('List sent', end="\n\r")

        if line[0] == 'put':
            filename = line[1]
            mes.receiveFile(filename, s_sock, BUFFSIZE)
            ok = "File received correctly"
            s_sock.sendto(ok.encode('utf8'), client)

        if line[0] == 'get':
            filename = line[1]
            print(f'Sending {filename}...')
            mes.sendFile(filename, s_sock, client, BUFFSIZE)

        if line[0] == 'exit':
            sys.exit(0)
except Exception as e:
    print(e)
finally:
    print('Closing socket', end="\n\r")
    s_sock.close()
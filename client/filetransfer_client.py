import socket, sys, time

BUFFSIZE = 4096
PORT = 10000

c_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('', PORT)
print('\n\r Choose between this commands: \n\r list of files \
    \n\r put <<file>> on server \n\r get <<file>> from server \
    \n\r exit the program')

try: 
    while True:
        message = input('\n\r Insert command: ')
        request = message.split()
        print('\n\r Sending %s to server' % message)
        sent = c_sock.send(message.encode(), server_address)
        print('\n\r Waiting to receive... ')
        data, server = c_sock.recvfrom(BUFFSIZE)
        line = data.decode('utf8').split()

        if request[0] == 'list':
            print('\n\r Here is the list of files: ')
            for i in line:
                print('\n\r %s' % i)
            
        if request[0] == 'put':
            filename = request[1]
        #if line == 'get':
        if line == 'exit':
            exit()

except Exception as info:
    print(info)
finally:
    print('\n\r Closing socket')
    c_sock.close()
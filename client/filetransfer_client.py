import socket
import sys
import messages as mes

BUFFSIZE = 4096
PORT = 10000

c_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.0', PORT)
print('\n\r Choose between this commands: \n\r list: list of the files in the server' +
    '\n\r put <<file>>: puts a file on server \n\r get <<file>>: gets a file from server' +
    '\n\r exit: exit the program')

try: 
    while True:
        message = ""
        while not message: 
            message = input('\n\r Insert command: ')
        c_sock.sendto(message.encode('utf8') , server_address)
        print('Waiting to receive...', end = "\n\r")
        list_message = message.split(' ', maxsplit=1)

        if list_message[0] == 'list':
            print('Here is the list of files: ', end = "\n\r")
            data, server = c_sock.recvfrom(BUFFSIZE)
            lines = data.decode('utf8').split()
            for line in lines:
                print(line)
            
        if list_message[0] == 'put':
            filename = list_message[1]
            print(f'Sending {filename}...')
            mes.sendFile(filename, c_sock, server_address, BUFFSIZE)
            print('File sent correctly', end="\n\r")
            c_sock.recvfrom(BUFFSIZE)

        if list_message[0] == 'get':
            filename = list_message[1]
            c_sock.sendto(filename.encode(), server_address)
            print(f'Sending {filename} request...')
            mes.receiveFile(filename, c_sock, BUFFSIZE)
            print('File received successfully.', end="\n\r")
        
        if message == 'exit':
            sys.exit(0)

except Exception as e:
    print(e)
finally:
    print('Closing socket', end="\n\r")
    c_sock.close()
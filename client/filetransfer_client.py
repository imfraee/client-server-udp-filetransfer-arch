import socket, sys, time
sys.path.append('/home/francesca/progetto_reti')
import messages as mes

BUFFSIZE = int(4096)
PORT = int(10000)

c_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', PORT)
print('\n\r Choose between this commands: \n\r list: list of the files in the server \
    \n\r put <<file>>: puts a file on server \n\r get <<file>>: gets a file from server \
    \n\r exit: exit the program')

try: 
    while True:
        message = input('\n\r Insert command: ')
        #print('\n\r Sending %s to server' % message)
        c_sock.sendto(message.encode('utf8') , server_address)
        print('\n\r Waiting to receive... ')
        list_message = message.split()

        if list_message[0] == 'list':
            print('\n\r Here is the list of files: ')
            data, server = c_sock.recvfrom(BUFFSIZE)
            line = data.decode('utf-8').split()
            i = 0
            for i in line[i]:
                print('\n\r %s' % i)
            
        if list_message[0] == 'put':
            filename = line[1]
            c_sock.sendto(filename, server_address)
            print("\n\r Sending %s..." % filename)
            mes.sendFile(filename, c_sock, server_address, BUFFSIZE)
            print("\n\r File sent correctly")
            c_sock.recvfrom(BUFFSIZE)

        if list_message[0] == 'get':
            filename = line[1]
            c_sock.sendto(filename, server_address)
            print("\n\r Sending %s request..." % filename)
            mes.receiveFile(filename, c_sock, BUFFSIZE)
            print("\n\r File received successfully.")
        
        if message == 'exit':
            exit()

except Exception as info:
    print(info)
finally:
    print('\n\r Closing socket')
    c_sock.close()
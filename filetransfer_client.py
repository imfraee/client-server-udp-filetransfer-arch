from email import message
import socket, sys, time

BUFFSIZE = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('', 10000)
message = sys.argv[1]

try: 
    print('\n\r Sending %s to server' % message)
    time.sleep(2)
    sent = sock.send(message.encode(), server_address)
    print('\n\r Waiting to receive... ')
    data, server = sock.recvfrom(BUFFSIZE)
    time.sleep(2)
    print('\n\r Received message %s' % data.decode('utf8'))
except Exception as info:
    print(info)
finally:
    print('\n\r Closing socket')
    sock.close()
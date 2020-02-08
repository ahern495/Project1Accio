import socket
import sys, getopt

def getInput():
    port = None
    fileDir = None

    argv = sys.argv[1:]

    port = argv[0]
    fileDir = argv[1]

sock = socket.socket()


sock.bind(127.0.0.1,port)
sock.listen()

fileName = input
blockSize = 1024

while True:
    connection, adress = sock.accept()
    file = open(inputFile, 'rb')
    data = file.read(blockSize)
    while data:
        connection.send(data)
        data = file.read(blockSize)
    file.close()
    print (fileName +' was successfully sent to '+str(address))
     connection.close()

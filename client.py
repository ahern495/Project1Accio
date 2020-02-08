import socket
import sys, getopt

def getInput():
    hostname = None
    port = None

    argv = sys.argv[1:]

    hostname = argv[0]
    port = argv[1]
    fileName = argv[2]

sock = socket.socket()

sock.connect ((hostname,port))

blockSize = 1024

while True:
    sckt, address = s.accept()

    print address
    i=1
    f = open(fileName,'wb') 
    i=i+1
    while (True):
        l = sc.recv(1024)
        while (l):
                f.write(l)
                l = sc.recv(1024)
    f.close()


    sckt.close()

sock.close()

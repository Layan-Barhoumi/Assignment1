import socket
from datetime import datetime

IP = "127.0.0.1"
port = 12345
BUFFER_SIZE = 4096

#create socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#bind
s.bind((IP,port))

data=""

#create infinite loop
while (True):

    #receive request from client
    data,addr=s.recvfrom(BUFFER_SIZE)
    
    #date-time syntax taken from example 3 (https://www.programiz.com/python-programming/datetime/current-datetime)
    if (data!=""):
        print ("Request received on ",datetime.now().strftime("%d/%m/%Y")," at ",datetime.now().strftime("%H:%M:%S"))
        s.sendto(data,addr)

s.close()
import socket
import time

IP = "127.0.0.1"
port = 12345
BUFFER_SIZE = 54    #size of "hello"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

RTT_sum = 0
for i in range (5):
    start_time = time.time()
    
    sock.sendto(str.encode("hello"),(IP,port))
    msg_received,address = sock.recvfrom(BUFFER_SIZE)
    
    end_time = time.time()

    RTT = end_time-start_time
    print ("RTT ["+str(i+1)+"] = "+str(RTT*(10**3))+" ms \n")
    RTT_sum+=RTT

avg = RTT_sum/5
print("Average RTT: "+str(avg)+" ms\n")

sock.close()

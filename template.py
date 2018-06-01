import socket
import sys

# create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connection info
server_address = ('chalbroker.cs1122.engineering.nyu.edu', 3120)
# connect to the server
sock.connect(server_address)

try:
	# receive data from the server
    print(sock.recv(1024))
    # tell the server who you are
    sock.send(str.encode("cz1529\n")) # your net id
	# receive confirmation from the server
    print(sock.recv(1024))
    
	# receive the challenge
    data = sock.recv(1024).decode("utf8")
    print(data)

	#
	# Solve the given challenge and return the answer as specified by the instructions
	#
    data2=[]
    data=data.splitlines()[1]
    data=[int(n) for n in data.split(',')]

    for i in range(len(data)-1,0,-1):
        for i in range(i):
            if data[i]>data[i+1]:
                data[i],data[i+1]=data[i+1],data[i]

	# send the server your answer
    data=" ".join(str(e) for e in data)
    print(data)
    sock.send(str.encode(data+"\n"))
    print(sock.recv(1024))

finally:
	# close the connection
    sock.close()

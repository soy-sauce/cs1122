import socket
import sys

# create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connection info
server_address = ('chalbroker.cs1122.engineering.nyu.edu', 3545)
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

    data = data.splitlines()
    print(data)
    n = int(data[0][4:])
    d = int(data[1][4:])
    c = int(data[2][4:])
    def exponent(c,d,n):
        if d==1:
            return c%n
        if d%2 !=0:
            return c*exponent(c,d-1,n)%n
        else:
            return exponent((c**2%n),d//2,n)

    answer=exponent(c,d,n)
    print(hex(answer))

	#
	# Solve the given challenge and return the answer as specified by the instructions
	#

	# send the server your answer
    sock.send(str.encode("answer"+"\n"))
finally:
	# close the connection
    sock.close()

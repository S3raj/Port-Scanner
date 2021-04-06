 #import socket
import socket 

#create socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#set timeout
s.settimeout(5)

#Taking inputs from the user 
# IPv4 address of the host 
# Port number to be scanned 
host = input("Please enter the host IP: ")
port = int(input("Please enter the port you want to scan: "))

#Function to connect with host and check if a particular port is open or closed
def portScanner(port):
	if s.connect_ex((host,port)):
		print("This port is closed")
	else: 
		print("This port is open")

portScanner(port)
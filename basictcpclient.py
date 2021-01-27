#Basic TCP Client

#Author: Lainey Tubbs
#Usage: Basic TCP client 

import socket

target_host = "www.google.com"
target_port = 80

client = socket.socket(socket.AF_INET, socket. SOCK_STREAM) #create socket object

#CONNECT THE CLIENT
client.connect((target_host,target_port)) #connect to the client. 

client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n") #send some data

response = client.recv(4096) #Receive some data

print response
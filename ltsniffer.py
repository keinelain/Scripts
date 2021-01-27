#Author: Lainey Tubbs
#Usage: Acts as a packet sniffer that listens to a host on a given ip address. 
#The program then determes the os by the protocol(s) accepted and then runs the scan. 

import socket
import os
host = "192.168.1.6" #The host to listen on

if os.name == "nt": #cREATES A RAW SCOKET AND BINDS IT TO THE PUBLIC INTERFACE
    socket_protocol = socket.IPPROTO_IP #if a windows environment, all packets will automatically be captured
else:
    socket_protocol = socket.IPPROTO_ICMP #If in a linux environment, it only listens to ICMP traffic. 

sniffer = socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

#socket.SOCK_RAW a raw socket.
#Socket module indicates what type of packets it can intercept. IPV4 packets fo socket.AF_INET

sniffer.bind((host,0))

sniffer.setsockopt(socket.IPPROTO_IP, SOCKET.ip_hdrincl, 1)

if os.name =="nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    
print(sniffer.recvfrom(65565))

if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF) #Turns of promiscuous mode for windows applications. 







#!/bin/bash 
#Usage: Simple Ping Sweep Script for subnet 192.168.122

echo "Enter the subnet you want to scan"
read SUBNET #assigns value to $SUBNET

for IP in $(seq 50 254); do
        ping -c 1 $SUBNET.$IP 2> /dev/null
done

~                                                                               
~              
#2021/01/12

#This is a port scanner with nmap integration so we can see the objects that 

import nmap
import optparse #module to add parsing options

def nmapScan(tgtHost,tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost,tgtPort)
    state=nmScan[tgtHost]['tcp'][int(tgtPort)]['state']

    print("*" + tgtHost + "tcp/"+tgtPort + " " + state

def main:
    parser = optparse.OptionParser('usage%prog' + '-H <target host> -p <target port>')

    parser.add_option('-H', dest='tgtHost', type='string' , help='specify target host')

    parser.add_option('-p', dest='tgtPort', type='string' , help='specify target port[s] with a comma')

    (options , args) = parser.parse_args()

    tgtHost = options.tgtHost

    tgtPorts = stry(options,tgtPort).split(',')

    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)

    for tgtPort in tgtPorts:
        nmapScan(tgtHost,tgtPort)

if __name__== ' __main__':
    main()

def miku():
    print('miku')



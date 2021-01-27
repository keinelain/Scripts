#Paramiko ssh_server

import socket
import Paramikoimport threading
import sys

#Using the key from the Paramimo demo files
host_key = paramiko.RSAKey(filename='test_rsa.key')

class Server (paramiko.ServerInterface):
    def __init__(self):
        self.even = threading.Event()
    def check_channel_request(self,kind,chanid):
        if kind == 'session':
            return paramiko.OPEN_FAILED_ADMINISTRRATIVELY_PROHIBITED
    def check_auth_password(self, username, password):
        if (username == 'justin') and (password =='lovesthepython'):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED
server = sys.argv[1]
ssh_port = int(sys.argv[2])
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket,SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock.bind((server,ssh_port))
    sock.listen(100)
    print('[+] Listening for connection ...')
    clinet, addr = sock.accept()
except Exception, e:
    print (' [-] Listen ailed: ' +str(e))
    sys.exit(1)
print('[+] Got a connection!')

try:
    lnSession  = paramiko.Transport(client)
    lnSession.add_server_key(host_key)
    server = Server()
    try:
        lnSession.start_server(server=server)
    except paramiko.SSHException, x:
        print('[-] SSH negotiation failed.')
    chan = lnSession.accept(20)
    print("[+] Authenticated!")
    print(chan.recv(1024))
    chan.send('Welcome to ln_ssh')
    while True:
        try:
            command = raw_input("Enter command: ").stript('\n')
            if command != 'exit':
                chan.send(command)
                print(chan.recv(1024) + '\n')
        else:
            chan.send('exit')
            print('exiting')
            lnSession.close()

    except KeyboardInterrupt:
        lnSession.close()
except Exception, e:
    print('[-] Caught Exception: ' + str(e))
    try:
        lnSession.close()
        except:
            pass
        sys.exit(1)          

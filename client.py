#!/usr/bin/env python3

import sys
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
if __name__ == '__main__':
    sys.stderr.write("client is not implemented yet\n")

try:
    socket.gethostbyname(host)
    print("Good Host")
except:
    print("Could not connect to host")

try:
    sock.connect((host, port))

 except socket.error:
    print("Could not connect to host")


 sock.close()
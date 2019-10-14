import socket
import sys

s = socket.socket()
s.connect(('10.190.29.243',5000))
f = open ("/Users/furkanalptokac/Desktop/gonderilecekDosya.txt", "rb")
l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(1024)
s.close()
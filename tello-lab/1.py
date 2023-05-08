import threading
import socket
import sys
import time
import platform
import get_key

host = ""
port = 9000
locale_addr = (host, port)
tello_addr = ("192.168.10.1", "8889")


# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(locale_addr)

sock.sendto(b'command', locale_addr)

sock.sendto(b"takeoff", locale_addr)
sock.sendto(b"left 25", locale_addr)
sock.sendto(b"backward 25", locale_addr)
sock.sendto(b"right 25", locale_addr)
sock.sendto(b"forward 25", locale_addr)


sock.sendto(b"battery?", locale_addr)
response, ip = sock.recvfrom(1024)

print(response)

sock.sendto(b"land", locale_addr)
sock.close()

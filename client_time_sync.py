# client_time_sync.py
import socket
import struct
import time

def sync_time(server_ip, port=9999):
    s = socket.socket()
    s.connect((server_ip, port))
    server_time = struct.unpack('d', s.recv(1024))[0]
    client_time = time.time()
    offset = server_time - client_time
    return offset

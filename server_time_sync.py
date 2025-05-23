# server_time_sync.py
from datetime import datetime
import socket
import struct
import time

def get_time():
    return time.time()

# Simple NTP response format
def send_time(conn):
    now = get_time()
    conn.sendall(struct.pack('d', now))

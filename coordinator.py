# coordinator.py
import socket
import time

def broadcast_play_time(devices, delay=3):
    play_at = time.time() + delay
    for device in devices:
        s = socket.socket()
        s.connect(device)
        s.sendall(str(play_at).encode())
        s.close()

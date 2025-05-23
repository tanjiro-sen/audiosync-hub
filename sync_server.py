import socket
import time

PORT = 8888
BROADCAST_IP = "255.255.255.255"
AUDIO_PLAY_DELAY = 3  # seconds

def broadcast_play_time():
    play_at = time.time() + AUDIO_PLAY_DELAY
    message = str(play_at).encode()

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto(message, (BROADCAST_IP, PORT))
    s.close()

    print(f"Broadcasted play time: {play_at}")

if __name__ == "__main__":
    broadcast_play_time()

# client_listener.py
import socket
from audio_player import play_audio_at

def listen_for_play_command(audio_path):
    s = socket.socket()
    s.bind(('', 8888))
    s.listen(1)
    conn, addr = s.accept()
    play_at = float(conn.recv(1024).decode())
    play_audio_at(audio_path, play_at)

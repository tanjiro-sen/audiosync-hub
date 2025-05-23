import socket
import time
import simpleaudio as sa

def play_audio_at(audio_path, play_at):
    while time.time() < play_at:
        time.sleep(0.001)
    sa.WaveObject.from_wave_file(audio_path).play()

def listen(audio_path="audio.wav"):
    s = socket.socket()
    s.bind(('', 8888))
    s.listen(1)
    print("Listening for sync signal...")
    conn, _ = s.accept()
    timestamp = float(conn.recv(1024).decode())
    conn.close()
    play_audio_at(audio_path, timestamp)

if __name__ == "__main__":
    listen()

import socket
import time
import simpleaudio as sa

def play_audio_at(audio_path, play_at):
    while time.time() < play_at:
        time.sleep(0.001)
    sa.WaveObject.from_wave_file(audio_path).play()

def listen_for_broadcast(audio_path="audio.wav"):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', 8888))
    print("Listening for sync broadcast...")

    while True:
        data, _ = s.recvfrom(1024)
        play_time = float(data.decode())
        print(f"Received sync time: {play_time}")
        play_audio_at(audio_path, play_time)

if __name__ == "__main__":
    listen_for_broadcast()

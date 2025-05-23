# audio_player.py
import simpleaudio as sa
import time

def play_audio_at(audio_path, play_at_timestamp):
    wave_obj = sa.WaveObject.from_wave_file(audio_path)
    while time.time() < play_at_timestamp:
        pass  # Busy wait or use sleep for less CPU load
    wave_obj.play()

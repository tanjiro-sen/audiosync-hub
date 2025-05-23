from flask import Flask, request
import time, socket

app = Flask(__name__)

@app.route("/sync", methods=["POST"])
def sync_audio():
    audio = request.files['audio']
    devices = request.form['devices'].split(",")
    delay = int(request.form['delay'])

    # Save audio to disk
    audio_path = "audio.wav"
    audio.save(audio_path)

    play_time = time.time() + delay
    for ip in devices:
        s = socket.socket()
        s.connect((ip.strip(), 8888))
        s.sendall(f"{play_time}".encode())
        s.close()

    return "Play signal sent", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

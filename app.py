import streamlit as st
import requests

st.set_page_config(page_title="SyncWave", layout="centered")

st.title("Audio Sync Playback Controller")

audio_file = st.file_uploader("Upload Audio File", type=["wav", "mp3"])
device_ips = st.text_input("Target Device IPs (comma-separated)")
delay = st.slider("Delay (seconds before playback)", 1, 10, 3)

if st.button("Start Sync") and audio_file and device_ips:
    with st.spinner("Sending sync command..."):
        files = {"audio": audio_file}
        data = {
            "devices": device_ips,
            "delay": delay
        }
        response = requests.post("http://localhost:5000/sync", files=files, data=data)
        if response.ok:
            st.success("Sync signal sent successfully.")
        else:
            st.error("Failed to send sync signal.")

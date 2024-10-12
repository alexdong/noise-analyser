import pyaudio
import numpy as np
import time
import csv
from datetime import datetime, timedelta
import os

# Function to measure noise level (decibels) using the microphone
def get_noise_level():
    # Microphone setup
    CHUNK = 1024  # Number of audio samples per frame
    RATE = 44100  # Sampling rate (44.1 kHz)
    
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)
    
    # Capture one frame of audio data
    data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    
    # Calculate the volume in decibels (dB)
    rms = np.sqrt(np.mean(np.square(data)))  # Root mean square of the audio signal
    db = 20 * np.log10(rms + 1e-6)  # Convert to decibels

    stream.stop_stream()
    stream.close()
    p.terminate()
    
    return db


def get_file_path():
    base_path = "/Users/alexdong/Library/Mobile Documents/com~apple~CloudDocs/noise_data"
    os.makedirs(base_path, exist_ok=True)
    current_time = datetime.now()
    if current_time.hour < 7:
        current_time -= timedelta(days=1)
    return os.path.join(base_path, f"{current_time.strftime('%Y-%m-%d')}.csv")

# Function to log noise levels to CSV
def log_noise_level():
    while True:
        file_path = get_file_path()
        file_exists = os.path.exists(file_path)
        
        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['Timestamp', 'Noise_Level_dB'])  # CSV headers

            while datetime.now().hour != 7 or datetime.now().minute != 0:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                noise_level = get_noise_level()  # Use microphone input
                print(f"{timestamp} - Noise Level: {noise_level:.2f} dB")
                writer.writerow([timestamp, noise_level])
                time.sleep(1)  # Log every second

        print(f"Logging rotated. New data will be saved to {get_file_path()}")

# Start logging noise levels continuously
log_noise_level()

import pyaudio
import numpy as np
import time
import csv
from datetime import datetime

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


# Function to log noise levels to CSV
def log_noise_level(file_path='noise_data.csv', duration_minutes=60):
    start_time = time.time()
    end_time = start_time + duration_minutes * 60

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Noise_Level_dB'])  # CSV headers

        while time.time() < end_time:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            noise_level = get_noise_level()  # Use microphone input
            print(f"{timestamp} - Noise Level: {noise_level:.2f} dB")
            writer.writerow([timestamp, noise_level])
            time.sleep(1)  # Log every second

    print(f"Logging complete. Data saved to {file_path}")

# Start logging noise levels for 8 hours (adjust as needed)
log_noise_level(duration_minutes=8*60)

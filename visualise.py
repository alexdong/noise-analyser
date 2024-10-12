import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import datetime, timedelta

# Function to visualize noise levels
def visualize_noise_data(date=None):
    base_path = "/Users/alexdong/Library/Mobile Documents/com~apple~CloudDocs/noise_data"
    
    if date is None:
        date = datetime.now().strftime('%Y-%m-%d')
    
    file_path = os.path.join(base_path, f"{date}.csv")
    
    if not os.path.exists(file_path):
        print(f"No data file found for {date}")
        return
    
    # Read the noise data CSV
    df = pd.read_csv(file_path)
    
    # Convert timestamp to datetime for plotting
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    
    # Plot the noise levels
    plt.figure(figsize=(10, 6))
    plt.plot(df['Timestamp'], df['Noise_Level_dB'], label='Noise Level (dB)', color='blue')
    plt.xlabel('Time')
    plt.ylabel('Noise Level (dB)')
    plt.title(f'Noise Levels for {date}')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Visualize the noise data for today (or specify a date)
visualize_noise_data()
# To visualize a specific date, use:
# visualize_noise_data('2024-10-13')

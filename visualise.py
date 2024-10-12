import matplotlib.pyplot as plt
import pandas as pd

# Function to visualize noise levels
def visualize_noise_data(file_path='noise_data.csv'):
    # Read the noise data CSV
    df = pd.read_csv(file_path)
    
    # Convert timestamp to datetime for plotting
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    
    # Plot the noise levels
    plt.figure(figsize=(10, 6))
    plt.plot(df['Timestamp'], df['Noise_Level_dB'], label='Noise Level (dB)', color='blue')
    plt.xlabel('Time')
    plt.ylabel('Noise Level (dB)')
    plt.title('Noise Levels Over Time')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Visualize the noise data
visualize_noise_data()

#Import the require modules
import pyaudio
import numpy as np
import matplotlib.pyplot as plt



#Function to play the audio
def play_audio(audio, sample_rate):
       p = pyaudio.PyAudio()
       stream = p.open(format=pyaudio.paFloat32,
                       channels=1,
                       rate=sample_rate,
                       output=True)
       stream.write(audio.tobytes())
       stream.stop_stream()
       stream.close()
       p.terminate()


#Load and process the audio file
def load_audio(file_path):
    audio = np.fromfile(file_path, dtype=np.float32)
    return audio



#Process audio
def process_audio(audio, sample_rate):
       # Apply any required processing to the audio here
       return audio


#Calculation the vibration strength
def calculate_vibration_strength(audio):
    # Convert audio to absolute values
    absolute_audio = np.abs(audio)
     # Calculate the average vibration strength for each time frame
    frame_size = 1024  # Adjust this value as per your preference
    num_frames = len(absolute_audio) // frame_size
    vibration_strength = np.zeros(num_frames)
    for i in range(num_frames):
        start = i * frame_size
        end = (i + 1) * frame_size
        frame = absolute_audio[start:end]
        vibration_strength[i] = np.mean(frame)
    return vibration_strength


#Visualize vibrations
def visualize_vibrations(vibration_strength):
       plt.plot(vibration_strength)
       plt.xlabel('Time')
       plt.ylabel('Vibration Strength')
       plt.show()

if __name__ == '__main__':
       file_path = 'sample.wav'  # Replace with your audio file path
       sample_rate = 1024  # Replace with the actual sample rate of your audio file
       audio = load_audio(file_path)
       processed_audio = process_audio(audio, sample_rate)
       vibration_strength = calculate_vibration_strength(processed_audio)
       visualize_vibrations(vibration_strength)
       play_audio(processed_audio, sample_rate)
import numpy as np
import soundfile as sf
from IPython.display import Audio
import scipy.signal as signal
import matplotlib.pyplot as plt
import sounddevice as sd

# Step 1: Load the Audio File
audio_file = 'guitar_loop.wav'  # Replace with your audio file
audio, sample_rate = sf.read(audio_file)

# Ensure mono audio (convert stereo to mono if needed)
if len(audio.shape) > 1:
    audio = audio[:, 0]  # Take the first channel

# Normalize the audio to [-1, 1]
audio = audio / np.max(np.abs(audio))

# Display audio information
print(f"Sample Rate: {sample_rate} Hz")
print(f"Audio Shape: {audio.shape}")

# Play the original audio
print("Playing Original Audio:")
sd.play(audio,sample_rate)

# Step 2: Design a Low-Pass Filter
cutoff_frequency = 2000  # Cutoff frequency in Hz
nyquist_rate = sample_rate / 2
num_taps = 101  # Number of filter coefficients

# Design the FIR filter
fir_coefficients = signal.firwin(num_taps, cutoff_frequency / nyquist_rate)

# Plot the filter's frequency response
w, h = signal.freqz(fir_coefficients, worN=8000)
plt.figure(figsize=(10, 6))
plt.plot((w / np.pi) * nyquist_rate, abs(h))
plt.title('Low-Pass Filter Frequency Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain')
plt.grid()
plt.show()

# Step 3: Apply the Filter
filtered_audio = signal.lfilter(fir_coefficients, 1.0, audio)

# Normalize the filtered audio to [-1, 1]
filtered_audio = filtered_audio / np.max(np.abs(filtered_audio))

# Step 4: Save and Play the Filtered Audio
sf.write('filtered_guitar_loop.wav', filtered_audio, sample_rate)
print("Playing Filtered Audio:")
sd.play(audio,sample_rate)

# Step 5: Frequency Domain Analysis
def plot_frequency_spectrum(audio, sample_rate, title):
    fft_result = np.fft.fft(audio)
    fft_freqs = np.fft.fftfreq(len(audio), d=1/sample_rate)
    
    # Take the positive frequencies
    pos_freqs = fft_freqs[:len(fft_result)//2]
    pos_magnitude = np.abs(fft_result[:len(fft_result)//2])
    
    # Plot the spectrum
    plt.figure(figsize=(10, 6))
    plt.plot(pos_freqs, pos_magnitude)
    plt.title(title)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.show()

# Plot original and filtered frequency spectra
plot_frequency_spectrum(audio, sample_rate, "Original Audio Frequency Spectrum")
plot_frequency_spectrum(filtered_audio, sample_rate, "Filtered Audio Frequency Spectrum")

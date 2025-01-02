import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf
import numpy as np
import scipy as sp
from scipy import signal

file_path = "bells.wav"

audio_data, samplerate = sf.read(file_path)

audio_data = audio_data [:, 1]
samplerate = 11025

size = np.size(audio_data)
duration = size / samplerate
time = np.arange(0, duration, 1/samplerate)

plt.title("Orginalni signal")
plt.xlabel("t(s)")
plt.grid()
plt.plot(time, audio_data)
plt.savefig("original.png")
plt.show()

noise = np.random.normal(0, 0.01, size)

plt.title("Bijeli šum")
plt.xlabel("t(s)")
plt.grid()
plt.plot(time, noise)
plt.savefig("noise.png")
plt.show()

noisy_audio = audio_data + noise

plt.title("Signal sa šumom")
plt.xlabel("t(s)")
plt.grid()
plt.plot(time, noisy_audio)
plt.savefig("noisy_audio.png")
plt.show()

hn = [-0.015, 0.058, -0.350, 1.000, -0.350, 0.058, -0.005]

convolution = signal.convolve(noisy_audio, hn, "same")

plt.title("Konačni signal")
plt.xlabel("t(s)")
plt.grid()
plt.plot(time, convolution)
plt.savefig("final.png")
plt.show()

print("Playing audio...")
sd.play(convolution, samplerate)
sd.wait()

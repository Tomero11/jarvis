import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

fs = 44100

print("Recording...")

recording = sd.rec(
    int(5 * fs),
    samplerate=fs,
    channels=1,
    dtype='int16'
)

sd.wait()

write("test.wav", fs, recording)

print("Saved test.wav")
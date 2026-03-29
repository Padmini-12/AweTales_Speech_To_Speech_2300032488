import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write

sample_rate = 16000
channels = 1

print("Press ENTER to start recording")
input()

print("Recording... Press ENTER to stop")

recording = []

def callback(indata, frames, time, status):
    recording.append(indata.copy())

stream = sd.InputStream(
    samplerate=sample_rate,
    channels=channels,
    callback=callback
)

with stream:
    input()

audio = np.concatenate(recording, axis=0)

audio = (audio * 32767).astype(np.int16)

write("speech.wav", sample_rate, audio)

print("Recording saved as speech.wav")
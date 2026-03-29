from transformers import pipeline
from scipy.io import wavfile
import numpy as np

print("Loading Whisper model...")

asr = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-small"
)

print("Model loaded")

sample_rate, audio = wavfile.read("speech.wav")

audio = audio.astype(np.float32) / 32768.0

result = asr(audio)

print("Transcription:")
print(result["text"])
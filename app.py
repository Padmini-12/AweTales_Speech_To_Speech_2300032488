import streamlit as st
from streamlit_mic_recorder import mic_recorder
from translate_text import translate_audio

st.title("Real-Time Speech Translation System")

# Language options
languages = ["Telugu", "Hindi", "Tamil", "French", "English", "Japanese"]
target_language = st.selectbox("Select Target Language", languages)

st.subheader("Record Speech")

audio = mic_recorder(
    start_prompt="Start Recording",
    stop_prompt="Stop Recording",
    key="mic"
)

# Save recorded audio
if audio:
    with open("speech.wav", "wb") as f:
        f.write(audio["bytes"])
    st.success("Recording captured!")
    st.audio("speech.wav")

# Upload audio file
st.subheader("Or Upload an Audio File")

uploaded_file = st.file_uploader(
    "Upload MP3 or WAV file",
    type=["wav", "mp3"]
)

if uploaded_file is not None:

    with open("speech.wav", "wb") as f:
        f.write(uploaded_file.read())

    st.success("File uploaded!")
    st.audio("speech.wav")

# Translate
if st.button("Translate Speech"):

    recognized, translated = translate_audio(target_language)

    st.subheader("Recognized Speech")
    st.write(recognized)

    st.subheader("Translated Text")
    st.write(translated)

    st.subheader("Translated Speech")
    st.audio("translated_audio.wav")
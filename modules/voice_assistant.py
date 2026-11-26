# ==========================================
# LifeOS - Multilingual Voice Assistant
# ==========================================

import streamlit as st
import tempfile
import os

from faster_whisper import WhisperModel


# Load Whisper model only once
@st.cache_resource
def load_whisper_model():

    model = WhisperModel(
        "base",
        device="cpu",
        compute_type="int8"
    )

    return model


# Convert recorded audio into text
def transcribe_audio(audio_file):

    if audio_file is None:
        return None, None

    model = load_whisper_model()

    # Save uploaded audio temporarily
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    ) as temp_audio:

        temp_audio.write(audio_file.getvalue())
        audio_path = temp_audio.name

    try:
        # Automatically detect spoken language
        segments, info = model.transcribe(
            audio_path,
            beam_size=5
        )

        # Combine recognized speech
        transcription = " ".join(
            segment.text.strip()
            for segment in segments
        )

        detected_language = info.language

        return transcription, detected_language

    finally:
        # Delete temporary audio file
        if os.path.exists(audio_path):
            os.remove(audio_path)


# Display microphone interface
def voice_input():

    st.subheader("🎙️ Talk to LifeOS")

    st.write(
        "Speak naturally in your preferred language."
    )

    audio = st.audio_input(
        "Record your voice"
    )

    if audio is not None:

        with st.spinner("Understanding your speech..."):

            text, language = transcribe_audio(audio)

        if text:

            st.success("Speech recognized!")

            st.write("*Detected language:*", language)

            st.write("*Your command:*", text)

            return text, language

        else:
            st.warning("No speech was recognized.")

    return None, None

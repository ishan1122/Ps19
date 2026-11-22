import io
import speech_recognition as sr

def transcribe_audio(audio_bytes: bytes) -> str:
    """Convert recorded WAV audio bytes from Streamlit into text."""
    if not audio_bytes:
        raise ValueError("No audio was recorded.")

    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(io.BytesIO(audio_bytes)) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        raise ValueError("Speech was unclear. Please record again and speak clearly.")
    except sr.RequestError as exc:
        raise RuntimeError(f"Speech recognition service is unavailable: {exc}")

    if not text.strip():
        raise ValueError("No speech was detected.")
    return text.strip()

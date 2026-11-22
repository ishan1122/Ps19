from io import BytesIO
from gtts import gTTS

def make_speech(text: str) -> bytes:
    """Convert assistant response text into MP3 audio bytes."""
    if not text or not text.strip():
        raise ValueError("There is no response text to speak.")
    audio_buffer = BytesIO()
    gTTS(text=text, lang="en", slow=False).write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer.read()

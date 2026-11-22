import streamlit as st
from dotenv import load_dotenv

from voice_input import transcribe_audio
from llm_response import get_llm_response
from text_to_speech import make_speech

load_dotenv()

st.set_page_config(page_title="Voice Assistant with LLM", page_icon="🎙️", layout="centered")

st.title("🎙️ Voice Assistant with LLM")
st.caption("Speak or type a question. The assistant transcribes it, generates an AI response, and can speak the answer.")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("About this project")
    st.write("PS19 – Voice Assistant with LLM")
    st.write("Speech-to-text: Google Web Speech recognition")
    st.write("LLM: Google Gemini")
    st.write("Text-to-speech: gTTS")
    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

st.subheader("1. Ask by voice")
audio_value = st.audio_input("Record your question")

if audio_value is not None:
    if st.button("Transcribe and ask", type="primary", use_container_width=True):
        with st.spinner("Transcribing your voice..."):
            try:
                question = transcribe_audio(audio_value.getvalue())
                st.success("Transcription complete")
                st.write("**You said:**", question)
                st.session_state.messages.append({"role": "user", "content": question})
            except Exception as exc:
                st.error(f"Could not transcribe the recording: {exc}")
                question = None

        if question:
            with st.spinner("Gemini is thinking..."):
                try:
                    history = st.session_state.messages[:-1]
                    answer = get_llm_response(question, history)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                    st.rerun()
                except Exception as exc:
                    st.error(str(exc))

st.divider()
st.subheader("2. Or type your question")
with st.form("text_question_form", clear_on_submit=True):
    typed_question = st.text_input("Your question", placeholder="For example: Explain artificial intelligence simply")
    submitted = st.form_submit_button("Ask assistant", type="primary", use_container_width=True)

if submitted:
    if not typed_question.strip():
        st.warning("Please enter a question.")
    else:
        st.session_state.messages.append({"role": "user", "content": typed_question.strip()})
        with st.spinner("Gemini is thinking..."):
            try:
                history = st.session_state.messages[:-1]
                answer = get_llm_response(typed_question.strip(), history)
                st.session_state.messages.append({"role": "assistant", "content": answer})
                st.rerun()
            except Exception as exc:
                st.error(str(exc))

if st.session_state.messages and st.session_state.messages[-1]["role"] == "assistant":
    st.divider()
    st.subheader("3. Listen to the latest answer")
    if st.button("Generate spoken answer", use_container_width=True):
        with st.spinner("Creating audio..."):
            try:
                audio_bytes = make_speech(st.session_state.messages[-1]["content"])
                st.audio(audio_bytes, format="audio/mp3")
                st.download_button("Download spoken answer", data=audio_bytes,
                                   file_name="assistant_reply.mp3", mime="audio/mpeg")
            except Exception as exc:
                st.error(f"Text-to-speech failed: {exc}")

st.caption("Note: Voice transcription uses Google's online speech recognition service and requires an internet connection.")

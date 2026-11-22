# PS19 – Voice Assistant with LLM
**Name:** [Your name]  
**Roll Number:** [Your roll number]  
**Class:** [Your class]  
**GitHub:** [Repository URL]

## 1. Problem statement
Typing is slow or inconvenient for some users. The project provides a voice-based chatbot that accepts spoken questions, converts speech into text, generates an answer using a Large Language Model (LLM), and speaks the answer aloud.

## 2. Tools and model
The application is developed in Python using Streamlit for the interface. SpeechRecognition with Google's online speech recognition service is used for speech-to-text. Google Gemini is used to generate answers. gTTS converts the generated text into MP3 audio. python-dotenv is used to load the API key securely from a local environment file.

## 3. Procedure
1. Installed Python and created a project folder.
2. Installed the required Python libraries using `pip install -r requirements.txt`.
3. Created a Gemini API key and stored it in a local `.env` file.
4. Implemented microphone audio transcription in `voice_input.py`.
5. Implemented the Gemini request and conversation context in `llm_response.py`.
6. Implemented audio generation in `text_to_speech.py`.
7. Built the Streamlit interface in `app.py` to record voice, show transcription, display the answer, accept typed questions, and play generated audio.
8. Ran the application using `streamlit run app.py`.
9. Tested voice and text questions and checked the generated responses and audio.

## 4. Prompt used
"You are a helpful, friendly voice assistant. Answer clearly and naturally. Keep answers concise unless the user asks for detail. Do not claim to perform actions you cannot perform."

**Prompt improvement:** Conversation history was added so the assistant can use recent context instead of treating every question as unrelated.

## 5. Results and testing
Add 1–2 screenshots of the running application here. Test at least five questions, including questions about AI, cloud computing, exam preparation, RAM versus storage, and a general question. Record whether transcription, answer generation, and audio playback worked for each test.

## 6. Challenges
Possible challenges include microphone permission, unclear recordings, internet connectivity, API key configuration, and API errors. These were addressed by adding error messages, checking the `.env` configuration, and allowing the user to record again or type a question.

## 7. Conclusion
The project demonstrates a basic voice assistant workflow using speech-to-text, an LLM, and text-to-speech. It supports voice and typed input and can speak the generated response. Its current limitations include dependence on internet services and English speech output. A future improvement could add multilingual speech recognition and selectable voices.

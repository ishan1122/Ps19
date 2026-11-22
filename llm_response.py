import os
from google import genai

def get_llm_response(question: str, history=None) -> str:
    """Send the user's question and recent conversation to Gemini."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is missing. Add it to your .env file.")

    client = genai.Client(api_key=api_key)
    history = history or []
    transcript = []
    for item in history[-8:]:
        role = "User" if item["role"] == "user" else "Assistant"
        transcript.append(f"{role}: {item['content']}")
    context = "\n".join(transcript)

    prompt = f"""You are a helpful, friendly voice assistant. Answer clearly and naturally.
Keep answers concise unless the user asks for detail. Do not claim to perform actions you cannot perform.

Previous conversation:
{context}

Current user question:
{question}

Assistant response:"""

    try:
        response = client.models.generate_content(
            model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
            contents=prompt
        )
        answer = (response.text or "").strip()
        if not answer:
            raise RuntimeError("Gemini returned an empty response. Please try again.")
        return answer
    except Exception as exc:
        raise RuntimeError(f"Gemini request failed: {exc}")

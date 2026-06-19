import os
import requests
from dotenv import load_dotenv

# Load .env file (keeps API keys out of code)
load_dotenv()

# ---------------- CONFIG ----------------
# Cloud LLM provider (Groq — free, fast, OpenAI-compatible)
# Set these as environment variables or Streamlit Cloud secrets
BASE_URL = os.getenv("LLM_BASE_URL", "https://api.groq.com/openai/v1")
LLM_API_KEY = os.getenv("LLM_API_KEY", "")
MODEL_NAME = os.getenv("LLM_MODEL_NAME", "llama-3.1-8b-instant")

TAVILY_KEY = os.getenv("TAVILY_API_KEY", "")


# ---------------- LLM CALL ----------------
def call_llm(system_msg: str, user_msg: str, max_tokens: int = 1000) -> str:
    headers = {"Content-Type": "application/json"}
    if LLM_API_KEY:
        headers["Authorization"] = f"Bearer {LLM_API_KEY}"

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg}
        ],
        "temperature": 0.3,
        "max_tokens": max_tokens,
        "top_p": 0.9,
    }

    try:
        response = requests.post(
            f"{BASE_URL}/chat/completions",
            json=payload,
            headers=headers,
            timeout=300
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"


# ---------------- TAVILY SEARCH ----------------
def tavily_search(query: str) -> list:
    if not TAVILY_KEY:
        return []

    try:
        r = requests.post(
            "https://api.tavily.com/search",
            json={"query": query, "max_results": 2},
            headers={"Authorization": f"Bearer {TAVILY_KEY}"},
            timeout=15
        )
        if r.status_code == 200:
            return r.json().get("results", [])
    except:
        pass

    return []

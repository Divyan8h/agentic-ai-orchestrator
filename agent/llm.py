# agent/llm.py
from langchain_groq import ChatGroq
import os

def get_llm(provider: str = "groq"):
    if provider == "groq":
        return ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama-3.3-70b-versatile",
            temperature=0
        )
    raise ValueError(f"Unsupported LLM provider: {provider}")

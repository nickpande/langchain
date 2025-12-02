import os
from langchain_google_genai import ChatGoogleGenerativeAI

def get_llm(model_name="gemini-pro-latest", temperature=0.7):
    """
    Returns a configured ChatGoogleGenerativeAI instance.
    """
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment variables.")
        
    llm = ChatGoogleGenerativeAI(
        model=model_name,
        temperature=temperature,
        google_api_key=google_api_key
    )
    return llm

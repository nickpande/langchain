import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from app.core.llm import get_llm

def main():
    print("Agentic AI Project Initialized")
    
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if google_api_key:
        print("Success: GOOGLE_API_KEY found. Environment variables loaded.")
        
        try:
            print("Initializing LLM...")
            llm = get_llm()
            print("Sending request to Gemini...")
            response = llm.invoke("Hello, Gemini! Tell me a fun fact about AI.")
            print("\nResponse from Gemini:")
            print(response.content)
        except Exception as e:
            print(f"Error calling LLM: {e}")
            
    else:
        print("Warning: GOOGLE_API_KEY not found in environment variables.")

if __name__ == "__main__":
    main()

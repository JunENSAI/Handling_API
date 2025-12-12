import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai

# 1. Load Environment Variables
load_dotenv()

# 2. Retrieve the Key securely
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("Error: GOOGLE_API_KEY not found in .env file.")
    sys.exit(1)

try:
    genai.configure(api_key=api_key)
except Exception as e:
    print(f"Configuration error: {e}", file=sys.stderr)

def run_gemini_example():
    print("--- Connecting to Google Gemini API ---")
    
    try:


        model = genai.GenerativeModel('gemini-2.5-flash')
        prompt = "What is API?"

        response = model.generate_content(
            contents=prompt
        )

        print("\n--- Response Received ---")
        if response.text:
            print(response.text)
        else:
            print("No text returned. Check safety filters or response structure.")

    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    run_gemini_example()
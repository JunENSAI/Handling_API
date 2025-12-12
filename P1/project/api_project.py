import os
import sys
import datetime
from dotenv import load_dotenv
import google.generativeai as genai

# 1. Setup & Authentication
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("Error: GOOGLE_API_KEY not found in .env file.")
    sys.exit(1)

try:
    genai.configure(api_key=api_key)
except Exception as e:
    print(f"Configuration error: {e}", file=sys.stderr)

def get_ai_summary(topic):
    """
    Sends the topic to Gemini and returns the text response.
    """

    model = genai.GenerativeModel('gemini-2.5-flash')

    prompt = (
        f"Explain the topic '{topic}' in simple terms. "
        "Then, provide 3 bullet points of 'Key Takeaways'. "
        "Keep the tone professional but easy to understand."
    )

    try:
        response = model.generate_content(
            contents=prompt
        )
        return response.text

    except Exception as e:
        print(f"\n[!] API Error: {e}")
        return None

def save_to_knowledge_base(topic, content):
    """
    Appends the research to a local Markdown file.
    """
    filename = "knowledge_base.md"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
 
    entry = (
        f"\n\n---\n"
        f"## Topic: {topic.title()}\n"
        f"**Date:** {timestamp}\n\n"
        f"{content}\n"
    )
    
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(entry)
        print(f"\n[✓] Saved to {filename}")
    except IOError as e:
        print(f"[!] File Error: {e}")

def main():
    print("--- AI Research Assistant (Powered by Gemini) ---")
    print("Type 'exit' to quit.\n")

    while True:
        topic = input("Enter a topic to research: ").strip()

        if topic.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break

        if not topic:
            continue

        print(f"Asking Gemini about '{topic}'...")
        
        # 1. Fetch
        summary = get_ai_summary(topic)
        
        if summary:
            # 2. Display
            print("\n--- AI Response ---")
            print(summary)
            
            # 3. Save
            save = input("\nSave this to knowledge base? (y/n): ").lower()
            if save == 'y':
                save_to_knowledge_base(topic, summary)
        
        print("\n" + "-"*30 + "\n")

if __name__ == "__main__":
    main()
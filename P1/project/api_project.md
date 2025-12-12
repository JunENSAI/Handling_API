## The Goal

Build a Python CLI tool that acts as your personal researcher. You enter a topic, and the tool uses Google's **Gemini models** to generate a concise summary and key facts, which are then saved to a `knowledge_base.md` file.

## Requirements

1.  **Authentication:** Securely load the `GOOGLE_API_KEY` from a `.env` file.

2.  **The API Interaction:** Use the `google-genai` SDK to send a specific system instruction ("You are a helpful tutor...").

3.  **Resilience:** Handle potential API errors (e.g., quota limits or connection drops).

4.  **Persistence:** Append the AI's answer to a Markdown file so you keep a history of everything you've learned.

## Prerequisites

1.  **API Key:** Ensure you have your Google AI Studio key.

2.  **Environment:** * `pip install google-genai python-dotenv`
    * Create `.env` file with `GOOGLE_API_KEY=...`
 
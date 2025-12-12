## 1. The Gatekeeper: Authentication
We access private or paid data. To do this, we need a "key."

### Types of Authentication
1.  **API Key:** A unique alphanumeric string that identifies the client (you). It's like a pass-card for a building.

2.  **OAuth2:** A complex flow involving temporary tokens (Access Tokens) and Refresh Tokens. Used when a user needs to log in with their account (e.g., "Login with Google").

---

### 2. Security Best Practice: The `.env` File

**Rule #1 of API Security:** Never commit your API keys to code repositories (GitHub, GitLab). 

If you write `client = Client(api_key="AIzaSy...")` and push it, bots will steal your key in seconds and drain your quota/credits.

**The Solution:** Environment Variables.

1.  We store secrets in a file named `.env` on your local computer.

2.  We tell our version control system (Git) to ignore this file via `.gitignore`.

3.  Our Python script reads this file only when it runs.

---

### 3. Raw HTTP vs. SDKs

For simple APIs, we use `requests` (Raw HTTP). For complex APIs (like Google Gemini, AWS, or Stripe), companies provide **SDKs** (Software Development Kits).

* **Raw HTTP:** You manually construct headers, JSON payloads, and handle 404 errors.

* **SDK:** You import a library (e.g., `google-genai`). It handles the connection, authentication headers, and JSON parsing for you, allowing you to work with Python objects directly.

In the python file, we use the `google-genai` SDK. Behind the scenes, this library is still sending `POST` requests with JSON, but it hides the complexity.

---
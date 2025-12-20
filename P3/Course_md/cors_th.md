## 1. What is CORS?
**CORS** (Cross-Origin Resource Sharing) is a security feature implemented by **Browsers**, not servers.

* **The Scenario:** You host your API on `api.mysite.com` (Port 8000). You host your frontend on `mysite.com` (Port 3000).

* **The Block:** By default, browsers block JS code on Port 3000 from reading data from Port 8000 to prevent malicious scripts from stealing data.

* **The Fix:** The Server must send a special header: `Access-Control-Allow-Origin: *` (or specific domain). This tells the browser: "It's okay, I trust this website."

---

## 2. OAuth2 (Conceptual)

You built JWT auth in Day 12. **OAuth2** is the standard for "Delegated Authorization".

* **Example:** "Log in with Google."

* **The Flow:**

    1.  User clicks "Login".

    2.  User is redirected to Google.

    3.  User says "Yes".

    4.  Google sends a **Code** back to your API.

    5.  Your API swaps that **Code** for an **Access Token**.

In Django, we rarely write this from scratch. We use libraries like `django-allauth` or `drf-social-oauth2`.

---
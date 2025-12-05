# The Architecture of the Web (HTTP & JSON)

Before writing Python code, we must understand the language of the web: **HTTP (HyperText Transfer Protocol)**.

### 1. The Client-Server Model

Everything in API development revolves around a conversation between two parties:

1.  **The Client:** The one asking for data (e.g., your Python script, a web browser, a mobile app).

2.  **The Server:** The one holding the data (e.g., Google's servers, a weather database).

This conversation follows a strict ruleset: **Request** and **Response**.

---

### 2. Anatomy of an HTTP Request
When you send a request, you must provide four main things:

* **URL (Endpoint):** Where are we going? (e.g., `https://api.github.com/users`)

* **Method (Verb):** What do we want to do?

    * `GET`: Retrieve data (Read).

    * `POST`: Send new data (Create).

    * `PUT`: Update existing data entirely (Replace).

    * `PATCH`: Update part of existing data (Modify).

    * `DELETE`: Remove data.
    
* **Headers:** Metadata about the request. (e.g., "I am sending JSON", "Here is my password").

* **Body (Payload):** The actual data being sent (used mostly in POST/PUT).

---

### 3. Anatomy of an HTTP Response

The server replies with:

* **Status Code:** A 3-digit number indicating success or failure.

    * `2xx` (Success): 200 OK, 201 Created.

    * `3xx` (Redirect): The resource moved.

    * `4xx` (Client Error): You made a mistake. 400 Bad Request, 401 Unauthorized, 404 Not Found.

    * `5xx` (Server Error): The server crashed. 500 Internal Server Error.

* **Body:** The requested data (usually in JSON format).

---

### 4. Lab Exercise: Manual Testing

**Goal:** Make a request without coding to see the raw data.

1.  Open **Postman** (or your browser).

2.  Enter URL: `https://httpbin.org/get`

3.  Ensure method is `GET`.

4.  Hit Send.

5.  Observe the JSON response.

---
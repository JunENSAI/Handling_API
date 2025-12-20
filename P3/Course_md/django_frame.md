## 1. The Philosophy

Django follows the "Batteries Included" philosophy. When you install Django, you get:

* An ORM (Database Manager).

* Authentication System.

* Admin Panel (GUI).

* Security (CSRF, XSS protection).

You don't have to choose libraries for these; they are built-in.

---

## 2. Project vs. App

In FastAPI, everything was often in one file. In Django, structure is king:

* **Project (`config`):** The folder containing settings (database config, global URLs).

* **Apps (`api`, `users`, `blog`):** Small, reusable modules that do specific things.

    * A Project contains many Apps.

---

## 3. Django REST Framework (DRF)

Django was built to generate HTML pages. To make it build APIs (JSON), we install a wrapper called **DRF**.

It gives us:

* **Serializers:** (Like Pydantic) Converts DB Models -> JSON.

* **ViewSets:** Controllers that handle logic.

* **Browsable API:** A generated UI (similar to Swagger) to browse your API.

---

## 4. The Request Cycle

1.  **URL (`urls.py`):** "Where does this request go?"

2.  **View (`views.py`):** "What logic should I run?"

3.  **Serializer (`serializers.py`):** "Format the data to JSON."

4.  **Response:** Send it back to the user.

---
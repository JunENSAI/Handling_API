## 1. Why FastAPI?

For years, Python developers used **Flask** (simple but slow) or **Django** (powerful but heavy). 

**FastAPI** is the modern standard because:

1.  **Speed:** It is as fast as NodeJS and Go (thanks to `Starlette` and `Pydantic`).

2.  **Async Native:** Built from the ground up to support `async` / `await`.

3.  **Auto-Documentation:** It automatically generates Swagger UI (interactive docs) for you.

---

## 2. The Tech Stack

To run a FastAPI app, you need two things:

1.  **FastAPI:** The framework that builds the app.

2.  **Uvicorn:** The lightning-fast ASGI web server that runs the app.

---

## 3. Type Hinting (The Secret Sauce)

FastAPI relies heavily on Python **Type Hints**.

* Standard Python: `def add(a, b):` (Python doesn't know if `a` is a number or text).

* Type Hinted: `def add(a: int, b: int) -> int:`

FastAPI reads these hints to automatically validate data. If a user sends text to an endpoint expecting an integer, FastAPI rejects it automatically with a clear error message. You don't write the validation `if` statements!

---

## 4. How to run it ?

Open your terminal and type :

```bash
uvicorn fastapi_intro:app
```

If you wanna try out the api, on the search bar add `/docs` to enter in the `Swagger`.

---
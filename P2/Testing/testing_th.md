## 1. Why Test?

Imagine you change a line of code in your Login logic. How do you know you didn't break the Registration logic?

* **Manual Way:** You open Postman, send a request, check the response, repeat 50 times. (Slow, boring, error-prone).

* **Automated Way:** You run `pytest`. 50 tests run in 0.5 seconds. Green means good. Red means you broke something.

---

## 2. The Tools

* **`pytest`:** The runner. It looks for files starting with `test_` and runs functions starting with `test_`.

* **`TestClient`:** A FastAPI tool (based on `httpx`). It lets you simulate HTTP requests to your API *without* actually running the Uvicorn server. It calls the Python function directly, which makes it incredibly fast.

---

## 3. The Anatomy of a Test

A test usually follows the **AAA Pattern**:

1.  **Arrange:** Prepare the data (e.g., create a dummy user).

2.  **Act:** Hit the API endpoint (`client.get("/items")`).

3.  **Assert:** Check the results (`assert response.status_code == 200`).

---

## 4. Testing Happy vs. Sad Paths

* **Happy Path:** The user does everything right (returns 200 OK).

* **Sad Path:** The user sends bad data (returns 400 or 422). You *must* test that your API fails gracefully.

---
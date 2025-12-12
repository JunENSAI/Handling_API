## 1. Synchronous vs. Asynchronous

Until now, our code has been **Synchronous** (Blocking).

* **The Model:** You go to a coffee shop. You order. The cashier stops serving everyone else, watches the machine brew your coffee, hands it to you, and *only then* takes the next order.

* **The Code:** `requests.get()` sends a signal and the entire Python script freezes until the server replies. If the server takes 2 seconds and you have 10 URLs, your script takes 20 seconds.

**Asynchronous** (Non-blocking) is the modern standard.

* **The Model:** You order coffee. The cashier gives you a buzzer and takes the next order immediately. When your coffee is ready, the buzzer rings.

* **The Code:** You fire off 10 requests instantly. You don't wait for the first to finish before starting the second. If the server takes 2 seconds, your script takes roughly 2 seconds total for all 10 URLs.

---

## 2. The Python Tools: `asyncio` & `httpx`

Standard Python uses `asyncio` to manage the "Event Loop" (the manager that handles the buzzers).

However, the `requests` library is **not** async-compatible. If you use it inside an async function, it will still block everything.

**Enter `httpx`:**

`httpx` is a modern library that looks exactly like `requests` but supports `async`.

* **Synchronous:** `client.get(url)`

* **Asynchronous:** `await client.get(url)`

---

## 3. The Keywords

* `async def`: Defines a function that can pause and wait for IO (Input/Output).

* `await`: The magic word. It means "Pause this function here, go do other work, and come back when the data arrives."
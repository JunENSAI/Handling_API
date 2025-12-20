## 1. What is Throttling?

Throttling (or Rate Limiting) restricts the number of requests a user can make within a specific timeframe.

* **Purpose:**

    1.  **Security:** Prevents DDoS attacks and Brute Force login attempts.

    2.  **Fairness:** Prevents one heavy user from slowing down the server for everyone else.

    3.  **Business:** You can charge money for higher limits (Freemium model).

---

## 2. DRF Throttling Scopes

Django REST Framework has built-in support for this.

* **AnonRateThrottle:** Limits unauthenticated users (by IP address).

* **UserRateThrottle:** Limits logged-in users (by User ID).

* **ScopedRateThrottle:** Limits specific parts of the API (e.g., "Login" is strict, "Read Posts" is loose).

---

## 3. The Response

When a user hits the limit, the API returns:

* **Status Code:** `429 Too Many Requests`

* **Body:** `"Request was throttled. Expected available in 56 seconds."`

---
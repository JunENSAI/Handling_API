## 1. Stateless Authentication (JWT)

In the old days, servers remembered logged-in users (Sessions). In modern APIs (Rest/FastAPI), the server is **stateless**. It remembers nothing.

**How it works:**

1.  User sends `username` + `password`.

2.  Server verifies them.

3.  Server generates a **Token** (a long string signed with a secret key) and gives it to the User.

4.  User attaches this Token to *every* future request (in the Header).

5.  Server checks the Token's signature. If valid, it lets the user in.

---

## 2. Hashing Passwords

**NEVER** store passwords in plain text. If your DB is hacked, everyone is compromised.

We use **Hashing** (turning "password123" into `$2b$12$G8...`).

* It is a one-way street. You cannot turn the hash back into the password.

* To verify, you hash the input and compare it to the stored hash.

---

## 3. Libraries

* `python-jose`: To generate and decode JWT tokens.

* `passlib`: To hash passwords securely (using bcrypt).

* `python-multipart`: To handle the login form data.

---
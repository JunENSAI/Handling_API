## 1. The Problem with Lists

In Crud_th if you restarted the server, all tasks vanished. To fix this, we need a database (DB).

---

## 2. What is an ORM?

Writing raw SQL (`SELECT * FROM users WHERE id=1`) is error-prone and specific to one DB type.

An **ORM (Object Relational Mapper)** allows you to interact with the DB using Python code.

* Python: `session.add(user)`

* SQL (Generated automatically): `INSERT INTO users ...`

---

## 3. SQLModel

SQLModel is the perfect match for FastAPI.

* **The Table:** Defines how data looks in the Database.

* **The Schema:** Defines how data looks in the API (Pydantic).

* **Unified:** In SQLModel, one class does both jobs.

---

## 4. Dependency Injection (`Depends`)

FastAPI has a powerful system called Dependency Injection.

We use it to manage Database Sessions.

* **The Goal:** Open a connection for a request, use it, and *guarantee* it closes afterwards, even if errors occur.

* **The Syntax:** `def create_hero(session: Session = Depends(get_session)):`
---
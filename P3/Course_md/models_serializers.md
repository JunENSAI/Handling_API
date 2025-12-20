## 1. The Model (The Database)

In Django, a **Model** is a Python class that represents a table in your database.

* You define fields (`charField`, `IntegerField`).

* Django automatically writes the SQL to create these tables (Migrations).

---

## 2. The Serializer (The Translator)

Your database speaks "Python Objects". Your API speaks "JSON".

A **Serializer** translates between them.

* **ModelSerializer:** The magic class. You tell it "Use the Book model", and it automatically generates fields for `id`, `title`, `author`, etc.

---

## 3. Migrations

Whenever you change a Model (e.g., add a `published_date` column), you must run two commands:

1.  `makemigrations`: Creates a script describing the change.

2.  `migrate`: Applies that script to the actual database.

---
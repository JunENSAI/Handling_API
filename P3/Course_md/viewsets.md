## 1. The Problem

Writing the same `get`, `post`, `put`, `delete` logic for every single table in your database is tedious and error-prone.

---

## 2. The Solution: ViewSets

A **ViewSet** is a class that includes the logic for *all* standard operations at once.

Instead of defining `get()`, you define `queryset = Book.objects.all()`. DRF does the rest.

----

## 3. The Router

If you use a ViewSet, you don't need to define URL paths manually (e.g., `path('books/', ...)`).

A **Router** automatically generates the URLs for you:

* `GET /books/` (List)

* `POST /books/` (Create)

* `GET /books/{id}/` (Retrieve)

* `PUT /books/{id}/` (Update)

* `DELETE /books/{id}/` (Destroy)

---
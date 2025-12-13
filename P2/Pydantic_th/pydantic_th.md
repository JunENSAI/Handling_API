## 1. The Problem with Raw JSON

When a user sends a JSON object to your API, how do you know it's correct?

* Did they forget the "email" field?

* Is "age" a number or text?

* Is the password long enough?

In older frameworks (Flask/Django), you wrote 20 lines of `if` statements to check this. In FastAPI, you use **Pydantic**.

---

## 2. Pydantic Models

Pydantic is a library that defines **Schemas**. A Schema is a blueprint that data *must* match.

```python
from pydantic import BaseModel

class User(BaseModel):
    username: str
    age: int
    is_active: bool = True  # Default value
```

If you tell FastAPI that an endpoint expects a `User`, it will:

- Read the JSON body.

- Convert "age": "25" (string) to 25 (integer) automatically.

- Throw a 422 Validation Error if required fields are missing.

---

## 3. Path vs. Query vs. Body

- `Path (/items/{id})`: Identifies a specific resource.

- `Query (/items?sort=desc)`: Sorts or filters resources.

- `Body (JSON)`: Sends content to be processed or saved (mostly for POST/PUT).

---

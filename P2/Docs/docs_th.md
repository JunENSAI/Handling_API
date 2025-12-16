## 1. The "Code-First" Philosophy

In the past, developers had to write a 50-page PDF to explain their API. It was always out of date.

FastAPI follows a **Code-First** approach: You write the Python code, and the documentation (OpenAPI Specification) is generated automatically.

---

## 2. Key Customization Areas

To make your docs professional, you need to touch three layers:

1.  **The Metadata:** Title, Description, Version, Terms of Service.

2.  **The Grouping:** Organizing messy endpoints into clean sections (e.g., "Users", "Items", "Auth") using **Tags**.

3.  **The Schemas:** Giving examples of what the data looks like (so users don't have to guess if "date" is `2023-01-01` or `01/01/2023`).

---

## 3. Pydantic `Field` & Examples

You can add help text directly to your data models.

```python
class Item(BaseModel):
    name: str = Field(
        title="Item Name", 
        description="The name must be unique.", 
        example="Ultra Widget 3000"
    )
```

---

## 4. Response Documentation

By default, FastAPI says `200 Successful Response`. You should explicitly document errors too.

```Python
@app.get("/items/{id}", responses={404: {"description": "Item not found"}})
```
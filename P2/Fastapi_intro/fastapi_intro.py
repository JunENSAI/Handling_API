from fastapi import FastAPI

# 1. Create the App Instance
app = FastAPI()

# 2. Define a Route (Endpoint)
# The decorator @app.get tells FastAPI this function handles GET requests
# at the root URL ("/")
@app.get("/")
def read_root():
    return {"message": "Hello World", "framework": "FastAPI"}

# 3. Path Parameters
# We can capture values from the URL using {variable_name}
# We use type hints (item_id: int) to enforce validation
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "is_even": item_id % 2 == 0}

# 4. Query Parameters
# If a variable is in the function arguments but NOT in the path string,
# FastAPI treats it as a Query Parameter (e.g., /search?q=apple)
@app.get("/search")
def search_items(q: str, limit: int = 10):
    return {"query": q, "limit": limit}
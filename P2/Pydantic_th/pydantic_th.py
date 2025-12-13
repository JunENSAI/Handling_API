from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

# 1. Define the Data Model (Schema)
class Item(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    description: Optional[str] = None
    price: float = Field(gt=0, description="Price must be greater than zero")
    tax: float = 10.5

# 2. POST Endpoint (Create)
@app.post("/items/")
def create_item(item: Item):
    total_price = item.price + item.tax
    
    return {
        "name": item.name,
        "final_price": total_price,
        "message": "Item validated and received!"
    }

# 3. Mixing Path, Query, and Body

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"query": q})
    return result
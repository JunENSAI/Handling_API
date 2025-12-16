from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

fake_db = []

class Item(BaseModel):
    name: str
    price: int

@app.get("/")
def read_root():
    return {"msg": "Hello World"}

@app.post("/items/", status_code=201)
def create_item(item: Item):
    if item.price < 0:
        raise HTTPException(status_code=400, detail="Price cannot be negative")
    fake_db.append(item)
    return item

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id >= len(fake_db) or item_id < 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]
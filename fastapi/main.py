from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Dict

app = FastAPI()
items: Dict[str, dict] = {}

class Item(BaseModel):
    id: str
    name: str

@app.get("/", response_class=HTMLResponse)
async def index():
    return """
    <h1>Welcome to the Item Management API!</h1>
    <h2>Available endpoints:</h2>
    <ul>
    <li><b>GET</b> /items - List all items</li>
    <li><b>POST</b> /items - Create a new item<br>
        &nbsp;&nbsp;Body: <code>{"id": str, "name": str}</code></li>
    <li><b>PUT</b> /items/{item_id} - Update an item name<br>
        &nbsp;&nbsp;Body: <code>{"name": str}</code></li>
    <li><b>DELETE</b> /items/{item_id} - Delete an item</li>
    </ul>
    """

@app.get("/items")
async def get_items():
    return list(items.values())

@app.post("/items", status_code=201)
async def create_item(item: Item):
    if item.id in items:
        raise HTTPException(status_code=409, detail="Item already exists")
    items[item.id] = item.dict()
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: str, data: dict):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    if "name" not in data:
        raise HTTPException(status_code=400, detail="Invalid input")
    items[item_id]["name"] = data["name"]
    return items[item_id]

@app.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
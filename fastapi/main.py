from fastapi import FastAPI, HTTPException, status, Body
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI(
    title="FastAPI REST API Example",
    description="A basic FastAPI project demonstrating REST API endpoints for GET, POST, PUT, and DELETE using in-memory storage.",
    version="1.0.0"
)

# In-memory storage
items: Dict[str, dict] = {}

class Item(BaseModel):
    """Model representing an item with an id and a name."""
    id: str
    name: str

class ItemUpdate(BaseModel):
    """Model for updating an item's name."""
    name: str

@app.get("/items", response_model=List[Item], summary="List all items", tags=["Items"])
def get_items():
    """Retrieve all items in the in-memory store."""
    return list(items.values())

@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED, summary="Create a new item", tags=["Items"])
def create_item(item: Item):
    """Create a new item. The id must be unique."""
    if item.id in items:
        raise HTTPException(status_code=409, detail="Item already exists")
    items[item.id] = item.dict()
    return item

@app.put("/items/{item_id}", response_model=Item, summary="Update an item's name", tags=["Items"])
def update_item(item_id: str, update: ItemUpdate = Body(...)):
    """Update the name of an existing item."""
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id]["name"] = update.name
    return items[item_id]

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete an item", tags=["Items"])
def delete_item(item_id: str):
    """Delete an item by its id."""
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
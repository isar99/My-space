from flask import Flask, request
from flask_smorest import abort
from db import stores, items
import uuid

app = Flask(__name__)

# Get all stores
@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}

# Get store using Store_ID
@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, description="Store not found")

# Create new store and return 429 if store already exists
@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    name_in_stores = []
    for val in stores.values():
        name_in_stores.append(val["name"])
    if store_data["name"] not in name_in_stores:
        store = {**store_data, "id" :store_id}
        stores[store_id] = store
        return store, 201
    return "Duplicate Stores", 429

# Update store name using store id
@app.put("/store/<string:store_id>")
def update_store(store_id):
    store_data = request.get_json()
    if "name" not in store_data:
        abort(400,
            description="Bad request. Ensure store name is provided")
    try:
        store = stores[store_id]
        store |= store_data
        return store, 201
    except KeyError:
        abort(404, message="Store not found.")

# Delete store using store id
@app.delete("/store/<string:store_id>")
def delete_store(store_id):
    try:
        del stores[store_id]
        return {"message": "Store deleted"}
    except KeyError:
        abort(404, message="Store not found.")

# Get all items
@app.get("/item")
def get_items():
    return {"items": list(items.values())}

# Create new item and return 429 if it already exists
@app.post("/item")
def create_item():
    item_data = request.get_json()
    if any(key not in item_data for key in ("price", "store_id", "name")):
        abort(400,
              description="Bad request. Ensure price, store_id and name are present")
    if item_data["store_id"] not in stores:
        abort(404, description="Store not found")
    name_in_items = []
    for val in items.values():
        name_in_items.append(val["name"])
    if item_data["name"] not in name_in_items:
        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}
        items[item_id] = item
        return item, 201
    return "Duplicate Items", 429

# Get item using item id
@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, description="Item not found")

@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message": "Item deleted."}
    except KeyError:
        abort(404, description="Item not found")

# Update item's price or name using item id
@app.put("/item/<string:item_id>")
def update_item(item_id):
    item_data = request.get_json()
    if any(key not in item_data for key in ("price", "name")):
        abort(400,
              description="Bad request. Ensure price and name are present in payload")
    try:
        item = items[item_id]
        item |= item_data
        return item, 201
    except KeyError:
        abort(404, "Item not found.")


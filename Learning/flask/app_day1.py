from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    },
    {
        "name": "My Store 2",
        "items": [
            {
                "name": "Couch",
                "price": 23.22
            },
            {
                "name": "Bed",
                "price": 25.32
            }
        ]
    }
]

@app.get("/stores")
def get_stores():
    return {"stores": stores}

@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201

@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"items": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404

@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "No store found"}, 404

@app.get("/store/<string:store_name>/items")
def get_items(store_name):
    for store in stores:
        if store["name"] == store_name:
            return store["items"]
    return {"message": "No store found"}, 404

@app.get("/store/<string:store_name>/item/<string:item_name>")
def get_price(store_name, item_name):
    for store in stores:
        if store["name"] == store_name:
            for item in store["items"]:
                if item["name"] == item_name:
                    return {"price": item["price"]}
                else:
                    return {"message": f"Item {item_name} not found in store {store_name}"}, 404
    else:
        return {"message": f"Store {store_name} not found"}, 404

# @app.put("/store/<string:store_name>/item/<string:item_name>/price")
# def update_price(store_name, item_name):
#     request_data = request.get_json()
#     new_price = request_data["price"]
#     for store in stores:
#         if store["name"] == store_name:
#             for item in store["items"]:
#                 if item["name"] == item_name:
#                     updated_item = {"price": new_price}
#                     return updated_item
#                 else:
#                     return {"message": f"Item {item_name} not found in store {store_name}"}, 404
#     else:
#         return {"message": f"Store {store_name} not found"}, 404




app.run(debug=True)

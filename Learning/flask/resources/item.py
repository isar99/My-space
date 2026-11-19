import uuid
from flask import request
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from db import stores, items

blp = Blueprint("items", __name__, description="Operations on Items")

blp.route("/item/<string:item_id>")
class Item(MethodView):
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, description="Item not found")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted."}
        except KeyError:
            abort(404, description="Item not found")

    def put(self, item_id):
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


@blp.route("/item")
class ItemList(MethodView):
    def get(self):
        return {"items": list(items.values())}

    def post(self):
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


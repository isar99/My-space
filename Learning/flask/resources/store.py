import uuid
from flask import request
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from db import stores

blp = Blueprint("stores", __name__, description="Operations on Stores")

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self,store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, description="Store not found")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted"}
        except KeyError:
            abort(404, message="Store not found.")
            
    def put(self,store_id):
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


@blp.route("/store")
class StoreList(MethodView):
    def get(self):
        return {"stores": list(stores.values())}

    def post(self):
        store_data = request.get_json()
        store_id = uuid.uuid4().hex
        name_in_stores = []
        for val in stores.values():
            name_in_stores.append(val["name"])
        if store_data["name"] not in name_in_stores:
            store = {**store_data, "id": store_id}
            stores[store_id] = store
            return store, 201
        return "Duplicate Stores", 429


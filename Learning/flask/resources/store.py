import uuid
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from schema import StoreSchema
from db import stores

blp = Blueprint("stores", __name__, description="Operations on Stores")

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
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

    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def put(self,store_data,store_id):
        try:
            store = stores[store_id]
            store |= store_data
            return 201, store
        except KeyError:
            abort(404, message="Store not found.")


@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return stores.values()

    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, store_data):
        store_id = uuid.uuid4().hex
        name_in_stores = []
        for val in stores.values():
            name_in_stores.append(val["name"])
        if store_data["name"] not in name_in_stores:
            store = {**store_data, "id": store_id}
            stores[store_id] = store
            return 201, store
        abort(429, description="Duplicate Stores")


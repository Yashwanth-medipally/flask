from flask import Flask,request
from db import stores,items

app=Flask(__name__)

stores={}
items={
    1:{
                "name":"chair",
                "price":159
            },
    2:{
                "name":"Table",
                "price":269
            }
}



@app.get("/store")
def get_stores():
    return {"stores":stores}

@app.post("/store")
def create_store():
    request_data=request.get_json()
    new_store={"name":request_data["name"],"items":[]}
    stores.append(new_store)
    return new_store, 201

@app.post("/store/<string:name>/item")
def create_item(name):
    request_data=request.get_json()
    for store in stores:
        if store["name"]==name:
            new_item={"name":request_data["name"], "price":request_data["price"]}
            store["items"].append(new_item)
            return new_item,201
    return {"message":"store not found"},404

@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {"message":"store not found"},404

@app.get("/store/<string:name>/item")
def get_store_items(name):
    for store in stores:
        if store["name"]==name:
            return {"items":store["items"]}
    return {"message":"store not found"},404


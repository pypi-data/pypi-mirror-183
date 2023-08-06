from fastapi import FastAPI
from pymongo import MongoClient
from src.mtgclient.db_client import MTGClient

user = 'root'
pswd = 'example'
host = '185.13.112.164:27017'
url = f'mongodb://{user}:{pswd}@{host}/'
client = MongoClient(url)

<<<<<<< HEAD
app = FastAPI(title="MTG_Client_Api", version="0.1.0")
=======

class Student:
    first_name: str
    last_name: str


app = FastAPI()
>>>>>>> db_realesation


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Customer
@app.post("/get_categories")
async def get_items():
    #list collections
    return {'items': list('a')}


@app.post("/get_items_in_cat")
async def get_items(category: str):
    # items in collection

    some_ans = {"poxuy": ['chemy']}
    return some_ans

# Admin
@app.post("/add_category")
async def get_items():
    #add collection
    return {'items': list('a')}


@app.post("/add_item_into_category")
async def get_items(category: str, name: str, description: str, cost: float):
    # add item
    return {'items': list('a')}


@app.get("/get_db_list/")
async def get_db_list(username, password, host):
    client = MTGClient(username=username, password=password, host=host)

    return client.db_list()
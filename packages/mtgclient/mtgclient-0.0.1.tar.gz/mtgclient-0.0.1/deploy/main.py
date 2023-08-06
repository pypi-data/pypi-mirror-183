# from pymongo import MongoClient


#
#
# username = 'root'
# password = 'example'
# host = '127.0.0.1'
#
# url = f'mongodb://{username}:{password}@{host}'
#
# client = MongoClient(url)
#
# db = client["test_databases"]
# coll = db["testcoll"]
#
# testdocument = { "name": "xyi"}
#
# x = coll.insert_one(testdocument)


from src.mtgclient.db_client import MTGClient
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def root():
    return FileResponse("deploy/vibor.html")
# curl http://127.0.0.1:8000/get_db_list/?username=root&password=example&host=127.0.0.1
# uvicorn deploy.main:app --reload --port 8000
@app.get("/get_db_list/")
async def get_db_list(username, password, host):
    client = MTGClient(username=username, password=password, host=host)

    return client.db_list()

# curl http://127.0.0.1:8000/get_coll_list/?username=root&password=example&host=127.0.0.1&company=tobacobunker
# uvicorn deploy.main:app --reload --port 8000

@app.get("/get_coll_list/")
async def get_coll_list(username, password, host, company):
    client = MTGClient(username=username, password=password, host=host)

    return client.get_collections(company=company)

# curl http://127.0.0.1:8000/get_data_list/?username=root&password=example&host=127.0.0.1&company=tobacobunker&product=одноразовые_электронки
# uvicorn deploy.main:app --reload --port 8000

@app.get("/get_data_list/")
async def get_data_list(username, password, host, company, product):
    client = MTGClient(username=username, password=password, host=host)

    return client.get_data(company=company, product=product)


# curl http://127.0.0.1:8000/get_create_db/?username=root&password=example&host=127.0.0.1&company=tobacobunker&product=одноразовые_электронки&item=hui

@app.get("/get_create_db/")
async def get_create_db(username, password, host, company, product, item):
    client = MTGClient(username=username, password=password, host=host)


    return client.create_db(company=company, product=product, item=item)

# curl http://127.0.0.1:8000/get_create_collection/?username=root&password=example&host=127.0.0.1&company=tobacobunker&product=одноразовые_электронки&item=hui
@app.get("/get_create_collection/")
async def get_create_collection(username, password, host, company, product, item):
    client = MTGClient(username=username, password=password, host=host)

    return client.create_collection(company=company, product=product, item=item)

# curl http://127.0.0.1:8000/get_create_data/?username=root&password=example&host=127.0.0.1&company=tobacobunker&product=одноразовые_электронки&item=hui

@app.get("/get_create_data/")
async def get_create_data(username, password, host, company, product, item):
    client = MTGClient(username=username, password=password, host=host)

    return client.create_data(company=company, product=product, item=item)

# curl http://127.0.0.1:8000/get_create_data/?username=root&password=example&host=127.0.0.1&company=tobacobunker&product=одноразовые_электронки&item=hui&nextitem=chleni

@app.get("/get_update_data/")
async def get_update_data(username, password, host, company, product, item, nextitem):
    client = MTGClient(username=username, password=password, host=host)

    return client.update_data(company=company, product=product, item=item, nextitem=nextitem)

# curl http://127.0.0.1:8000/get_delete_db/?username=root&password=example&host=127.0.0.1&company=tobacobunker

@app.get("/get_delete_db/")
async def get_delete_db(username, password, host, company):
    client = MTGClient(username=username, password=password, host=host)

    return client.delete_db(company=company)

# curl http://127.0.0.1:8000/get_delete_collection/?username=root&password=example&host=127.0.0.1&company=tobacobunker&product=одноразовые_электронки

@app.get("/get_delete_collection/")
async def get_delete_collection(username, password, host, company, product):
    client = MTGClient(username=username, password=password, host=host)

    return client.delete_collection(company=company, product=product)

# curl http://127.0.0.1:8000/get_delete_data/?username=root&password=example&host=127.0.0.1&company=tobacobunker&product=одноразовые_электронки&item=chleni

@app.get("/get_delete_data/")
async def get_delete_data(username, password, host, company, product, item):
    client = MTGClient(username=username, password=password, host=host)

    return client.delete_data(company=company, product=product, item=item)


# import gridfs

# client = MTGClient()
# connection = client.db_connection()

# db = connection["tobacobunker"]
# fs = gridfs.GridFS(db)
#
# file = rx"C:\Users\Nastya\Desktop\ABFH8904.jpeg"
# with open(file, 'rb') as f:
#     content = f.read()
# fs.put(content, filename="file")


# db = connection["tobacobunker"]
# coll = db["одноразовые_электронки"]
#
# for x in db.list_collections():
#     print(x)





# client.delete_collection("tobacobunker", "одноразовые_электронки")
# client.delete_db("tobacobunker")
# client.delete_data("tobacobunker", "sokromente", "electronsmoke")
# client.db_list()
# client.update_data("tobacobunker", "sokromente", "admin", "meshchera", "doc", "doc")
# client.create_db("tobacobunker", "sokromente", "meshchera")
# client.create_collection("tobacobunker", "hyi", "электронная сигарета", "наименование")
# client.insert_data("tobacobunker", "sokromente", "meshchera")
# client.delete_datadoc("tobacobunker", "sokromente", "admin", "meshchera", "doc", "doc")
# client.create_data("tobacobunker", "одноразовые_электронки", "наименование", "UDN", "кол-во затяжек", "2000", "вкус", "чай", "цена", "650", "описание", "емкость аккумулятора: 950 аккумулятор: встроеный страна: китай производитель: жопа крепость: 19,9мг тип затяжки: сигаретная")
# client.addmassive("tobacobunker", "sokromente", "электронки", "meshchera", "doc", "doc")
# client.delete_collection("tobacobunker", "одноразовые_электронки")
# client.get_data("tobacobunker", "одноразовые_электронки")
# client.get_collections("tobacobunker")


# db = connection["test"]
# coll = db["coll"]

# names = {"name": "doker"}
# newname = {"$set": {"name": "doc"}}

# coll.update_one(names, newname)

# db = connection["test"]
# coll = db["coll1"]
# document = {"name": "doc1"}



# for db in connection.list_databases():
#     print(db)




# from mtgclient.db_client import MTGClient
# client = MTGClient()
# connection = client.db_connection()
# db = client.create_db()
# collection = client.create_collectio








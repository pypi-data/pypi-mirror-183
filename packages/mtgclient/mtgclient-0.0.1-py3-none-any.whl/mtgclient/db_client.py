from pymongo import MongoClient


class MTGClient:
    '''
    Client to realise business logic
    source: https://www.mongodb.com/docs/manual/crud/
    '''
    def __init__(self, username='root', password='example', host='127.0.0.1') -> None:
        '''
        Initiate of db connections
        '''

        self.username = username
        self.password = password
        self.host = host

    def db_connection(self):
        '''
        Create a connection object with database
        :input:
            db_host - location of database server
            user_name - db username
            pswd - user password
        :return:
            Connection object
        '''

        url = f'mongodb://{self.username}:{self.password}@{self.host}'

        client = MongoClient(url)
        return client

    def create_db(self, company, product, item):
        '''
        Create db in mongo server
        :return:
        '''

        connection = self.db_connection()

        db = connection[company]
        coll = db[product]

        administration = {"admin": item}

        a = coll.insert_one(administration)

    def delete_db(self, company):
        '''
        Delete db in mongo server
        :return:
        '''
        connection = self.db_connection()
        connection.drop_database(company)

    def db_list(self):
        '''
        Output of databases
        :input:
        :return:
        '''
        connection = self.db_connection()
        dbs = []
        for db in connection.list_databases():
            print(db)
            dbs.append(db["name"])
        return dbs

    def create_collection(self, company, product, item):
        '''
        Get list of collections
        :input:
        name - collection name
        :return:
            collections[list] - list of collections
        '''
        connection = self.db_connection()

        db = connection[company]
        coll = db[product]

        document = {"admin": item}

        x = coll.insert_one(document)

    def create_data(self, company, product, item):
        '''
        create data document
        '''

        connection = self.db_connection()

        db = connection[company]
        coll = db[product]

        document = {"admin": item}

        x = coll.insert_one(document)

    def insert_data(self, company, product, address):
        '''
        Get list of collections
        :input:
        :return:
            collections[list] - list of collections
        '''

        connection = self.db_connection()

        db = connection[company]
        coll = db[product]



        adm = [
            {"admin": address},
            {"name": "Roman"}
        ]

        d = coll.insert_many(adm)

    def update_data(self, company, product, item, nextitem):
        '''
        Get list of collections
        :input:
        :return:
            collections[list] - list of collections
        '''
        connection = self.db_connection()
        db = connection[company]
        coll = db[product]

        firstname = {"admin": item}
        nextname = {"$set": {"admin": nextitem}}

        coll.update_one(firstname, nextname)

    def addmassive(self, company, branch, docname, firstdoc, nextdocname, nextdoc):
        '''
        Get list of collections
        :input:
        :return:
            collections[list] - list of collections
        '''
        connection = self.db_connection()
        db = connection[company]
        coll = db[branch]

        firstname = {docname: firstdoc}
        nextname = {"$push": {nextdocname: nextdoc}}

        coll.update_one(firstname, nextname)

    def delete_datadoc(self, company, branch, docname, firstdoc, nextdocname, nextdoc):
        '''delete string document'''

        connection = self.db_connection()
        db = connection[company]
        coll = db[branch]

        firstname = {docname: firstdoc}
        nextname = {"$unset": {nextdocname: nextdoc}}

        coll.update_one(firstname, nextname)

    def get_collections(self, company):
        '''
        Get list of collections
        :input:
        :return:
            collections[list] - list of collections
        '''

        connection = self.db_connection()
        colls = []
        db = connection[company]
        for coll in db.list_collections():
            print(coll)
            colls.append(coll["name"])
        return colls

    def get_data(self, company , product):
        '''
        Function acting with DB to make an analog of SELECT operation. It returns a choosing data.
        :input:
            collection_name - name of mongo collection

        :return:
            data[dict] - dict of returned data from db corresponding querry's conditions
        '''
        connection = self.db_connection()

        db = connection[company]
        coll = db[product]
        item = {}
        datas = []

        for data in coll.find():
            print(data.keys())
            item['наименование'] = data['наименование']
            item['кол-во затяжек'] = data['кол-во затяжек']
            item['вкус'] = data['вкус']
            item['цена'] = data['цена']
            item['описание'] = data['описание']
            datas.append(item)
        return datas

    def delete_collection(self, company, product):
        '''
        Delete collection
        :input:

        :return:
            status[str] - success or exeption
        '''
        connection = self.db_connection()
        db = connection[company]
        db.drop_collection(product)

    def delete_data(self, company, product, item):
        '''
        Delete data
        :input:
        :return:
        '''
        connection = self.db_connection()
        db = connection[company]
        coll = db[product]
        document = {"admin": item}
        coll.delete_one(document)

        # from mtgclient.db_client import MTGClient
        # from fastapi import FastAPI, Form
        # from fastapi.responses import FileResponse
        #
        # app = FastAPI()
        #
        # @app.get("/")
        # async def root():
        #     return FileResponse("deploy/vibor.html")
        #
        # # curl http://127.0.0.1:8000/get_db_list/?username=root&password=example&host=127.0.0.1
        # # uvicorn deploy.main:app --reload --port 8000
        # @app.get("/get_db_list/")
        # async def get_db_list(username, password, host):
        #     client = MTGClient(username=username, password=password, host=host)
        #
        #     return client.db_list()
        #
        # # curl http://127.0.0.1:8000/get_coll_list/?username=root&password=example&host=127.0.0.1&company=tobacobunker
        # # uvicorn deploy.main:app --reload --port 8000
        #
        # @app.get("/get_coll_list/")
        # async def get_coll_list(username, password, host, company):
        #     client = MTGClient(username=username, password=password, host=host)
        #
        #     return client.get_collections(company=company)
        #
        # # curl http://127.0.0.1:8000/get_data_list/?username=root&password=example&host=127.0.0.1&company=tobacobunker&product=одноразовые_электронки
        # # uvicorn deploy.main:app --reload --port 8000
        #
        # @app.get("/get_data_list/")
        # async def get_data_list(username, password, host, company, product):
        #     client = MTGClient(username=username, password=password, host=host)
        #
        #     return client.get_data(company=company, product=product)
        #
        # # curl http://127.0.0.1:8000/get_create_db/?username=root&password=example&host=127.0.0.1&company=tobacobunker&product=одноразовые_электронки&item=hui
        #
        # @app.get("/get_create_db/")
        # async def get_create_db(username, password, host, company, product, item):
        #     client = MTGClient(username=username, password=password, host=host)
        #
        #     return client.create_db(company=company, product=product, item=item)
        #
        # # curl http://127.0.0.1:8000/get_create_collection/?username=root&password=example&host=127.0.0.1&company=tobacobunker&product=одноразовые_электронки&item=hui
        # @app.get("/get_create_collection/")
        # async def get_create_collection(username, password, host, company, product, item):
        #     client = MTGClient(username=username, password=password, host=host)
        #
        #     return client.create_collection(company=company, product=product, item=item)
        #
        # # curl http://127.0.0.1:8000/get_create_data/?username=root&password=example&host=127.0.0.1&company=tobacobunker&product=одноразовые_электронки&item=hui
        #
        # @app.get("/get_create_data/")
        # async def get_create_data(username, password, host, company, product, item):
        #     client = MTGClient(username=username, password=password, host=host)
        #
        #     return client.create_data(company=company, product=product, item=item)
        #
        # # curl http://127.0.0.1:8000/get_create_data/?username=root&password=example&host=127.0.0.1&company=tobacobunker&product=одноразовые_электронки&item=hui&nextitem=chleni
        #
        # @app.get("/get_update_data/")
        # async def get_update_data(username, password, host, company, product, item, nextitem):
        #     client = MTGClient(username=username, password=password, host=host)
        #
        #     return client.update_data(company=company, product=product, item=item, nextitem=nextitem)
        #
        # # curl http://127.0.0.1:8000/get_delete_db/?username=root&password=example&host=127.0.0.1&company=tobacobunker
        #
        # @app.get("/get_delete_db/")
        # async def get_delete_db(username, password, host, company):
        #     client = MTGClient(username=username, password=password, host=host)
        #
        #     return client.delete_db(company=company)
        #
        # # curl http://127.0.0.1:8000/get_delete_collection/?username=root&password=example&host=127.0.0.1&company=tobacobunker&product=одноразовые_электронки
        #
        # @app.get("/get_delete_collection/")
        # async def get_delete_collection(username, password, host, company, product):
        #     client = MTGClient(username=username, password=password, host=host)
        #
        #     return client.delete_collection(company=company, product=product)
        #
        # # curl http://127.0.0.1:8000/get_delete_data/?username=root&password=example&host=127.0.0.1&company=tobacobunker&product=одноразовые_электронки&item=chleni
        #
        # @app.get("/get_delete_data/")
        # async def get_delete_data(username, password, host, company, product, item):
        #     client = MTGClient(username=username, password=password, host=host)
        #
        #     return client.delete_data(company=company, product=product, item=item)

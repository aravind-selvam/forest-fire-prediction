import pymongo


class mongodbconnection:
    # This class shall be used for mongoDB operation
    def __init__(self, username, password):
        try:
            self.username = username
            self.password = password
            self.url = f"mongodb+srv://{self.username}:{self.password}@cluster0.bisvs.mongodb.net/?retryWrites=true&w=majority"
        except Exception as e:
            raise e

    def getMongoClient(self):
        # It creates connection with the database
        try:
            client = pymongo.MongoClient(self.url)
            return client
        except Exception as e:
            raise e

    def getDatabase(self, dbName):
        # Gives database
        try:
            client = self.getMongoClient()
            database = client[dbName]
            return database
        except Exception as e:
            raise e

    def getCollection(self, dbName, collectionName):
        # Gives collection of a database
        try:
            database = self.getDatabase(dbName)
            collection = database[collectionName]
            return collection
        except Exception as e:
            raise e

    def getdata(self, dbName, collectionName):
        try:
            database = self.getDatabase(dbName)
            collection = database[collectionName]
            all_records = collection.find()
            list_cursor = list(all_records)
            return list_cursor
        except Exception as e:
            raise e

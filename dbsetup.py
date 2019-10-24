import sys
import json
import pymongo
import traceback


class Database:
    def __init__(self):
        self.url  = "mongodb://localhost:27017/"
        self.db   = "polling"
        self.col  = "input"

    def connection(self):
        myclient = pymongo.MongoClient(self.url)
        mydb = myclient[self.db]
        self.mycol = mydb[self.col]

    def document(self):
        try:
            return self.mycol.insert_many([
                                        { "_id": 0, "name": "Miguel de Cervantes", "vote": 0 },
                                        { "_id": 1, "name": "Charles Dickens", "vote": 0 },
                                        { "_id": 2, "name": "J.R.R. Tolkien", "vote": 0 },
                                        { "_id": 3, "name": "Antoine de Saint-Exuper", "vote": 0 }
                                    ]).inserted_id
        except:
            return "Failed"

    def update(self, data):
        try:
            self.mycol.update({"name": data}, { '$inc': {"vote": 1}})
        except:
            return "Failed"

    def get_data(self):
        try:
            return self.mycol.find({}, {'_id': False})
        except:
            return []
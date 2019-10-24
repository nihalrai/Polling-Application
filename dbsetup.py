import pymongo
import traceback


class Database:
    def __init__(self):
        self.url  = "mongodb://localhost:27017/"
        self.db   = "SAMPLE"
        self.col  = "INPUT"

    def connection(self):
        myclient = pymongo.MongoClient(self.url)
        mydb = myclient[self.db]
        mycol = mydb[self.col]
        return mycol

    def document(self):
        try:
            mycol = self.connection()
            return mycol.insert_many({
                                        {
                                            "name": "Miguel de Cervantes",
                                            "vote": 0
                                        },
                                        {
                                            "name": "Charles Dickens",
                                            "vote": 0
                                        },
                                        {
                                            "name": "J.R.R. Tolkien",
                                            "vote": 0
                                        },
                                        {
                                            "name": "Antoine de Saint-Exuper",
                                            "vote": 0
                                        }}).inserted_id
        except:
            return "Failed"

    def update(self, data):
        try:
            mycol = self.connection()
            mycol.update({"name": data}, { '$inc': {"vote": 1}})
        except:
            return "Failed"

    def get_data(self):
        try:
            mycol = self.connection()
            return mycol.find({}, {'_id': False})
        except:
            traceback.print_exc()
            return []
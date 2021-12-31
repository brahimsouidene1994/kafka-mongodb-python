import pymongo


def insert_new_user(obj, col_name):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["users_database"]
    col = db[col_name]
    x = col.insert_one(obj)
    return x


def fetch_all_user(col_name):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["users_database"]
    col = db[col_name]
    return col.find()

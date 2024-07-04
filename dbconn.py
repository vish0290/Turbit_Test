from pymongo import MongoClient

try:
    client = MongoClient("mongodb://mongodb:27017/")
    db = client['turbit_db']
    user_db = db['users']
    comment_db = db['comments']
    post_db = db['posts']

except:
    print("Could not connect to MongoDB")
    exit()
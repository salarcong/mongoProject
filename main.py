from config import URL
from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient(URL)
    database = client['cursoMongoDB']
    collection = database['users']
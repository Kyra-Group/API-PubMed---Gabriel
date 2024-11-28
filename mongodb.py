from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["pubmed_db"]

def save_to_mongodb(articles: list):
    collection = db["articles"]
    result = collection.insert_many(articles)
    return result.inserted_ids

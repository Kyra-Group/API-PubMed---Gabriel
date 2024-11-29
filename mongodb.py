from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["pubmed_db"]

def save_to_mongodb(articles: list):
    if not isinstance(articles, list) or not articles:
        raise ValueError("El argumento 'articles' debe ser una lista no vacía")

    collection = db["articles"]
    try:
        result = collection.insert_many(articles, ordered=False) # Insertar artículos en MongoDB
        return [str(_id) for _id in result.inserted_ids] # Convertir ObjectId a string para que FastAPI pueda convertir las respuestas a JSON
    except Exception as e:
        print(f"Error al guardar en MongoDB: {e}")
        return []

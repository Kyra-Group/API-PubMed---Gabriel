from fastapi import FastAPI, HTTPException
from pubmeds import search_pubmed, fetch_details
from mongodb import save_to_mongodb
import traceback # Para saber qué da error
from bson import ObjectId

def serialize_article(article):
    """
    Convierte el ObjectId del campo '_id' a string.
    """
    if "_id" in article and isinstance(article["_id"], ObjectId):
        article["_id"] = str(article["_id"])
    return article

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API de PubMed con MongoDB de Gabriel"}

@app.get("/search/")
async def search(termino_busqueda: str):
    try:
        ids = search_pubmed(termino_busqueda)
        print("Lista de ids para subir a la bdd: ", ids)
        articles = fetch_details(ids)
        print("Artículos que se van a subir a la bdd: ", articles)
        ids_insertados = save_to_mongodb(articles)
        print("IDs insertados en MongoDB: ", ids_insertados)
        articulos_serializados = [serialize_article(article) for article in articles]
        return {
            "message": "Artículos guardados en MongoDB",
            "inserted_ids": ids_insertados,
            "articles": articulos_serializados
        }
    
    except Exception as e:
        # Imprime la traza completa del error
        print("Error procesando la solicitud:")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

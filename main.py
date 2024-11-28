from fastapi import FastAPI, HTTPException
from pubmeds import search_pubmed, fetch_details
from mongodb import save_to_mongodb

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API de PubMed con MongoDB de Gabriel"}

@app.get("/search/")
async def search(termino_busqueda: str):
    try:
        ids = search_pubmed(termino_busqueda)
        articles = fetch_details(ids)
        save_to_mongodb(articles)
        return {"message": "Artículos guardados en MongoDB", "articles": articles}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

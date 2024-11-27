from fastapi import FastAPI, Query, HTTPException
import httpx

app = FastAPI()
app.title = "API Pubmed - Gabriel"

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API PubMed"}


@app.get("/", tags=['Resultados']) # Creamos una ruta básica
async def root():
    return {"message": "Hello World"}

@app.get("/Búsqueda", tags=['Búsqueda'])
async def busqueda_pubmed(keyword: str = Query(..., descripcion = "Palabra filtro para buscar artículos")):
    
    esearch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    efetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    esearch_parametros = {
        "term": keyword,
        "retmode": "json",
    }
    async with httpx.AsyncClient() as client: # ?????
        # Realiza la solicitud esearch para obtener los ID de artículos
        esearch_response = await client.get(esearch_url, params=esearch_parametros)
        if esearch_response.status_code != 200:
            raise HTTPException(status_code=500, detail="Error en la solicitud a PubMed esearch")
        
        esearch_data = esearch_response.json()
        idlist = esearch_data['esearchresult']['idlist']
        
        if not idlist:
            return {"message": f"No se encontraron artículos para la palabra clave '{keyword}'."}
        

    efetch_parametros = {
        "db": "pubmed",
        "id": ",".join(idlist),  # IDs separados por comas
        "retmode": "xml",  # Formato de respuesta para artículos
    }

    efetch_response = await client.get(efetch_url, params=efetch_parametros)
    if efetch_response.status_code != 200:
            raise HTTPException(status_code=500, detail="Error en la solicitud a PubMed efetch")
        
        # Procesa los datos de efetch (en este caso en formato XML, puedes usar JSON si disponible)
    efetch_data = efetch_response.text
        # Para un procesamiento más avanzado, necesitarías analizar el XML o cambiar a JSON si lo soporta
        
        # Aquí puedes agregar un filtro para buscar el `keyword` en el título
        # NOTA: Requiere análisis del texto recibido o cambiar a JSON si es soportado.
        
    return {
         "keyword": keyword,
         "idlist": idlist,
           "details": efetch_data,  # Devuelve los detalles en texto crudo por simplicidad
    }
import requests

# Definimos la URL base de la API de PubMed
url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

# Parámetros de la solicitud, por ejemplo, una búsqueda simple por palabra clave
params = {
    "term": "cáncer",
    "retmode": "json",
}

# Realizamos la solicitud GET
response = requests.get(url, params=params)

# Compruebo si la solicitud fue exitosa
if response.status_code == 200:
    # Parseamos la respuesta JSON
    data = response.json()
else:
    print("Error en la solicitud", response.status_code)



print(data['esearchresult']['idlist'])
idlist_results = data['esearchresult']['idlist']
url_detalles = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
parametros = {
    "db": "pubmed",  # Base de datos
    "id": ",".join(idlist_results),  # IDs separados por comas
    "retmode": "json",  # Formato de respuesta
}
response = requests.get(url_detalles, params=parametros)

if response.status_code == 200:
    # Guardamos los datos en una nueva variable
    articles_details = response.json()
    print("Esto es articles_details: ",articles_details)  # Imprime el nuevo JSON con los detalles
else:
    print("Error en la solicitud", response.status_code)
print(articles_details['result'])
# resultados = articles_details['result']
# for uid in result["uids"]:
#     article = result[uid]  # Accede a los detalles del artículo
#     title = article.get("title", "No disponible")  # Título de la publicación
#     authors = [author["name"] for author in article.get("authors", [])]  # Lista de autores
#     abstract = article.get("abstract", "No disponible")  # Resumen o descripción
    
#     print(f"Título: {title}")
#     print(f"Autores: {', '.join(authors)}")
#     print(f"Resumen: {abstract}")
#     print("-" * 40)

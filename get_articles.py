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

# Comprobamos si la solicitud fue exitosa
if response.status_code == 200:
    # Parseamos la respuesta JSON
    data = response.json()
    print(data)
else:
    print("Error en la solicitud", response.status_code)

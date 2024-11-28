import requests

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def search_pubmed(termino_busqueda: str):
    url = f"{BASE_URL}esearch.fcgi"
    params = {"db": "pubmed", "term": termino_busqueda, "retmode": "json"}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()["esearchresult"]["idlist"]

def fetch_details(ids: list):
    url = f"{BASE_URL}efetch.fcgi"
    params = {"db": "pubmed", "id": ",".join(ids), "retmode": "json"}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

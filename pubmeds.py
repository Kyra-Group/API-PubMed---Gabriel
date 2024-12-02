import requests
import xml.etree.ElementTree as ET

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def search_pubmed(termino_busqueda: str):
    url = f"{BASE_URL}esearch.fcgi"
    params = {"db": "pubmed",
               "term": termino_busqueda,
                 "retmode": "json"
                 }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()["esearchresult"]["idlist"]

def fetch_details(ids: list):
    url = f"{BASE_URL}efetch.fcgi" 
    params = {"db": "pubmed",
               "id": ",".join(ids),
                 "retmode": "xml"
                 }
    response = requests.get(url, params=params)
    response.raise_for_status()
    try:
        root = ET.fromstring(response.text)
        articles = []
        for article in root.findall(".//PubmedArticle"):
            title = article.find(".//ArticleTitle").text if article.find(".//ArticleTitle") is not None else "No title"
            abstract = article.find(".//AbstractText").text if article.find(".//AbstractText") is not None else "No abstract"
            authors = []
            for author in article.findall(".//Author"):
                last_name = author.find("LastName").text if author.find("LastName") is not None else ""
                fore_name = author.find("ForeName").text if author.find("ForeName") is not None else ""
                full_name = f"{fore_name} {last_name}".strip()
                if full_name:  # Solo agregar si hay un nombre
                    authors.append(full_name)

            articles.append({
                "title": title,
                "abstract": abstract,
                "authors": authors or ["No authors available"]})
        
        return articles
    except ET.ParseError as e:
        print("Error parseando XML:", e)
        raise ValueError("Error procesando la respuesta de la API (formato incorrecto).")

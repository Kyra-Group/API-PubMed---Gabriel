# PubMed Data Extractor and Storage

Este repositorio contiene un proyecto diseñado para interactuar con la API de PubMed (Entrez Programming Utilities), extrayendo datos relevantes de publicaciones científicas para su almacenamiento en local, utilizando MongoDB como base de datos.

## Tabla de Contenidos

1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Características](#características)
3. [Requisitos](#requisitos)
4. [Instalación](#instalación)
5.
---

## Descripción del Proyecto

El objetivo de este proyecto es facilitar la búsqueda y extracción de publicaciones científicas de PubMed. Se implementa un flujo automatizado para:
- Buscar publicaciones relevantes utilizando palabras clave.
- Extraer detalles completos de las publicaciones (títulos, autores, resúmenes, etc.).
- Almacenar los datos en una base de datos local MongoDB.

El repositorio también incluye configuración para un flujo de despliegue CI/CD, asegurando un entorno de desarrollo ágil y confiable.

---

## Características

- **Búsqueda de publicaciones**: Utiliza el endpoint `esearch.fcgi` para buscar publicaciones relevantes en PubMed.
- **Obtención de detalles**: Usa el endpoint `efetch.fcgi` para extraer información detallada basada en PMIDs.
- **Opciones de almacenamiento**: Integra MongoDB para gestionar y consultar los datos de forma estructurada.
- **Automatización con CI/CD**: Configuración de GitHub Actions para pruebas y despliegues continuos.

---

## Requisitos

- **Python 3.8+**
- **Dependencias de Python**:
  - `requests`
  - `pymongo` (para interactuar con MongoDB)
- **MongoDB**: Instalado y configurado en local.
- Cuenta de GitHub para integrar con Actions y CI/CD.

---

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu-usuario/pubmed-data-extractor.git
   cd pubmed-data-extractor

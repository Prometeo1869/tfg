# Importar los módulos necesarios
import requests
import pandas as pd

# Definir la URL de la API
url = "https://imdb-top-100-movies.p.rapidapi.com/"

# Definir los encabezados necesarios para hacer una solicitud a la API
headers = {
    "X-RapidAPI-Key": "1ef09404c0msha8762538d43bb96p1e0e55jsn18bf1e4617a1",
    "X-RapidAPI-Host": "imdb-top-100-movies.p.rapidapi.com"
}

# Hacer una solicitud GET a la URL especificada y pasar los encabezados necesarios
response = requests.get(url, headers=headers)
# Obtener los datos JSON de la respuesta
json_data = response.json()
# Crear un DataFrame a partir de los datos JSON
df = pd.DataFrame(json_data)


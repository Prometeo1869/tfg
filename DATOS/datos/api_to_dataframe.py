import requests
import pandas as pd

url = "https://imdb-top-100-movies.p.rapidapi.com/"

headers = {
	"X-RapidAPI-Key": "1ef09404c0msha8762538d43bb96p1e0e55jsn18bf1e4617a1",
	"X-RapidAPI-Host": "imdb-top-100-movies.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
json_data = response.json()
df = pd.DataFrame(json_data)

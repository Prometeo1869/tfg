from flask import Flask
from database import get_filmes_data

app = Flask(__name__)

@app.route('/movies')
def my_movies():
    # Obtener los datos de la tabla filmes como un DataFrame
    df = get_filmes_data()
    # Convertir el DataFrame en un objeto JSON
    movies_json = df.to_json(orient='records')
    # Devolver el objeto JSON como respuesta
    return movies_json

if __name__ == '__main__':
    app.run(debug=True, port=5000)


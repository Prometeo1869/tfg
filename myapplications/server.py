from flask import Flask, request
import pandas as pd
from database import get_filmes_data, get_engine

app = Flask(__name__)

# Esta función se ejecuta cuando se hace una petición POST a la ruta '/movies'
@app.route('/movies', methods=['POST'])
def add_movie():
    # Obtener los datos de la nueva película del cuerpo de la petición
    movie_data = request.get_json()
    # Crear un nuevo DataFrame con los datos de la película
    new_movie = pd.DataFrame([movie_data])
    # Obtener un objeto engine para interactuar con la base de datos
    engine = get_engine()
    # Insertar los datos de la nueva película en la tabla filmes
    new_movie.to_sql('filmes', engine, if_exists='append', index=False)
    # Devolver un mensaje de éxito como respuesta
    return 'Movie added successfully!'

# Esta función se ejecuta cuando se hace una petición GET a la ruta '/movies'
@app.route('/movies', methods=['GET'])
def get_all_movies():
    # Obtener los datos de la tabla filmes como un DataFrame
    df = get_filmes_data()
    # Convertir el DataFrame en un objeto JSON
    movies_json = df.to_json(orient='records')
    # Devolver el objeto JSON como respuesta
    return movies_json

# Esta función se ejecuta cuando se hace una petición GET a la ruta '/movies/<movie_id>'
@app.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie_by_id(movie_id):
    # donde <movie_id> es un número entero que representa el id de la película que se quiere obtener
    # Obtener los datos de la tabla filmes como un DataFrame
    df = get_filmes_data()
    # Filtrar el DataFrame para obtener solo la fila que coincida con el id especificado
    movie = df.loc[df['id'] == movie_id]
    # Convertir el resultado en un objeto JSON
    movie_json = movie.to_json(orient='records')
    # Devolver el objeto JSON como respuesta
    return movie_json

# Esta función se ejecuta cuando se hace una petición PUT a la ruta '/movies/<movie_id>'
@app.route('/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    # Obtener los nuevos datos de la película del cuerpo de la petición
    movie_data = request.get_json()
    # Crear un nuevo DataFrame con los datos de la película
    updated_movie = pd.DataFrame([movie_data])
    # Obtener un objeto engine para interactuar con la base de datos
    engine = get_engine()
    # Crear una conexión a la base de datos
    conn = engine.connect()
    # Definir la sentencia SQL para actualizar los datos de la fila que coincida con el id especificado
    update_statement = f"UPDATE filmes SET title = '{updated_movie['title'].iloc[0]}', rating = {updated_movie['rating'].iloc[0]}, year = {updated_movie['year'].iloc[0]}, image = '{updated_movie['image'].iloc[0]}', genre = '{updated_movie['genre'].iloc[0]}', director = '{updated_movie['director'].iloc[0]}' WHERE id = {movie_id}"
    # Ejecutar la sentencia SQL
    conn.execute(update_statement)
    # Cerrar la conexión a la base de datos
    conn.close()
    # Devolver un mensaje de éxito como respuesta
    return 'Movie updated successfully!'

# Esta función se ejecuta cuando se hace una petición DELETE a la ruta '/movies/<movie_id>'
@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    # Obtener un objeto engine para interactuar con la base de datos
    engine = get_engine()
    # Crear una conexión a la base de datos
    conn = engine.connect()
    # Definir la sentencia SQL para eliminar la fila que coincida con el id especificado
    delete_statement = f"DELETE FROM filmes WHERE id = {movie_id}"
    # Ejecutar la sentencia SQL
    conn.execute(delete_statement)
    # Cerrar la conexión a la base de datos
    conn.close()
    # Devolver un mensaje de éxito como respuesta
    return 'Movie deleted successfully!'


# Este bloque de código se ejecuta solo si este archivo se ejecuta directamente (no si se importa como un módulo)
if __name__ == '__main__':
    # Iniciar el servidor Flask en modo debug y en el puerto 5000
    app.run(debug=True, port=5000)

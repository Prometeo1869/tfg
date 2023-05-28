# Importar el DataFrame df del módulo api_to_dataframe
from api_to_dataframe import df

# Función para obtener un DataFrame con los datos que quiero usar
def get_filmes_df():
    # Seleccionar solo algunas columnas del DataFrame df y copiarlas en un nuevo DataFrame
    my_df = df[['id', 'title', 'rating', 'year', 'image']].copy()
    # Agregar una columna id al nuevo DataFrame y establecer su valor igual al índice de cada fila
    my_df['id'] = my_df.index
    # Cambiar el tipo de datos de la columna rating a float
    my_df['rating'] = my_df['rating'].astype(float)
    # Agregar una columna genre al nuevo DataFrame y llenarla con el primer elemento de la lista de géneros de cada película
    my_df['genre'] = df['genre'].apply(lambda x: x[0])
    # Agregar una columna director al nuevo DataFrame y llenarla con el primer elemento de la lista de directores de cada película
    my_df['director'] = df['director'].apply(lambda x: x[0])
    # Devolver el nuevo DataFrame
    return my_df

# Importar las funciones que se usaran de los módulos database y dataframe
from database import get_engine, create_filmes_table
from dataframe import get_filmes_df

# Llamar a la función create_filmes_table para crear una tabla en la base de datos
create_filmes_table()

# Obtener un objeto engine utilizando la función get_engine
engine = get_engine()
# Obtener un DataFrame utilizando la función get_filmes_df
my_df = get_filmes_df()
# Guardar los datos del DataFrame en la tabla filmes de la base de datos
my_df.to_sql('filmes', con=engine, if_exists='append', index=False)

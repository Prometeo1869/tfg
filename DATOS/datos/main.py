from database import get_engine, create_filmes_table
from dataframe import get_filmes_df

create_filmes_table()

engine = get_engine()
my_df = get_filmes_df()
my_df.to_sql('filmes', con=engine, if_exists='append', index=False)
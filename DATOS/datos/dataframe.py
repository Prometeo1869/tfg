from api_to_dataframe import df

def get_filmes_df():
    my_df = df[['id', 'title', 'rating', 'year', 'image']].copy()
    my_df['id'] = my_df.index
    my_df['rating'] = my_df['rating'].astype(float)
    my_df['genre'] = df['genre'].apply(lambda x: x[0])
    my_df['director'] = df['director'].apply(lambda x: x[0])
    return my_df
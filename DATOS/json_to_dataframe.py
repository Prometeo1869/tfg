import pandas as pd
from api_to_dataframe import json_data

df = pd.DataFrame(json_data)

df.head(5)
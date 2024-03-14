import requests
import pandas as pd

response = requests.get("https://pokeapi.co/api/v2/pokemon/?limit=151")

json_data = response.json()
table_data = pd.json_normalize(json_data['results'])

print(table_data)

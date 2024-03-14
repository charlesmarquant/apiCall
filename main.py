import requests
import pandas as pd

## Call API
response = requests.get("https://pokeapi.co/api/v2/pokemon/?limit=151")

## Put json data into a table
json_data = response.json()
table_data = pd.json_normalize(json_data['results'])

## Print table
print(table_data)

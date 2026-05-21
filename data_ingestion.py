import requests
import pandas as pd

url="OUR_API"

response=requests.get(url)

data=response.json()

rows=[]

for item in data:

    row={
        "name":item["name"],
        "price":item["price"],
        "genre":item["genre"],
        "rating":item["rating"]
    }

    rows.append(row)

df=pd.DataFrame(rows)

df.to_csv(
    "data/raw/data.csv",
    index=False
)

clean=pd.read_csv(
    "data/raw/data.csv"
)

clean=clean.drop_duplicates()

clean=clean.dropna()

clean.to_csv(
    "data/processed/clean.csv",
    index=False
)
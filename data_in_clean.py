import os
import requests
import pandas as pd
from dotenv import load_dotenv


load_dotenv()

EIA_API_KEY = os.getenv("EIA_API_KEY")
FRED_API_KEY = os.getenv("FRED_API_KEY")

RAW_PATH = "data/raw/"



def fetch_eia_data(endpoint, params): # Generic API request helper
    """
    Sends request to EIA API
    returns JSON response
    """
    base_url = f"https://api.eia.gov/v2/{endpoint}"
    params["api_key"] = EIA_API_KEY
    response = requests.get(base_url,params=params)
    response.raise_for_status()
    return response.json()



def json_to_dataframe(json_data): # Convert JSON -> DataFrame
    rows = json_data["response"]["data"]
    df = pd.DataFrame(rows)
    return df


def save_raw(df, filename): # Save DataFrame
    path = f"{RAW_PATH}{filename}"
    df.to_csv(
        path,
        index=False
    )
    print(f"Saved: {path}")


# Regular Gas Prices
gas_params = { 

    "frequency": "weekly",

    "data[0]": "value",

    "facets[product][]": "EPMR",

    "sort[0][column]": "period",

    "sort[0][direction]": "desc",

    "length": 5000
}


gas_json = fetch_eia_data(
    "petroleum/pri/gnd/data/",
    gas_params
)
gas_df = json_to_dataframe(gas_json)
save_raw(gas_df,"gas_prices.csv")


# National weekly prices
state_params = {

    "frequency": "weekly",

    "data[0]": "value",

    "facets[product][]": "EPMR",

    "facets[duoarea][]": "NUS",

    "sort[0][column]": "period",

    "sort[0][direction]": "asc",

    "length": 5000
}

state_json = fetch_eia_data("petroleum/pri/gnd/data/",state_params)

state_df = json_to_dataframe(state_json)

save_raw(state_df,"national_prices.csv")


# Crude oil prices

oil_params = {

    "frequency": "weekly",

    "data[0]": "value",

    "facets[series][]": "RWTC",

    "sort[0][column]": "period",

    "sort[0][direction]": "desc",

    "offset": 0,

    "length": 5000
}


oil_json = fetch_eia_data("petroleum/pri/spt/data/",oil_params)

oil_df = json_to_dataframe(oil_json)

save_raw(oil_df,"crude_oil.csv")


def fetch_fred_data(series_id, start_date="2015-01-01"): # FRED API 
    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {

        "series_id": series_id,

        "api_key": FRED_API_KEY,

        "file_type": "json",

        "observation_start": start_date
    }

    response = requests.get(url,params=params)
    response.raise_for_status()
    return response.json()


def fred_to_dataframe(json_data): # FRED JSON -> DataFrame
    rows = json_data["observations"]
    df = pd.DataFrame(rows)
    return df


# US Inflation (CPI)
# CPIAUCSL:
# Consumer Price Index for All Urban Consumers
# --------------------------------

inflation_json = fetch_fred_data(
    "CPIAUCSL"
)

inflation_df = fred_to_dataframe(
    inflation_json
)

save_raw(
    inflation_df,
    "inflation.csv"
)
print("\nFinished ingesting")
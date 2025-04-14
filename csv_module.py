#%%
import pandas as pd
import requests 
from io import StringIO
from sqlalchemy import create_engine
import json

# Load configuration
with open('config.json') as file:
    config = json.load(file)["warehouse"]

def csv_downloader(csv_url):
    try:
        print("Connecting to data source...")
        response = requests.get(csv_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        
        print("Reading CSV data...")
        data = StringIO(response.text)
        df = pd.read_csv(data)
        return df
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
        return None        
        
def send_data_to_db(df, table_name):
    print(f"Connecting to database...")
    user_name = config['user']
    pw = config['password']
    host = config['host']
    port = config['port']
    db = config['database']
    
    db_url = f'postgresql://{user_name}:{pw}@{host}:{port}/{db}'
    engine = create_engine(db_url)
    
    print(f"Uploading {len(df)} rows to {table_name}...")
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    
    print(f"Successfully created {table_name} table")
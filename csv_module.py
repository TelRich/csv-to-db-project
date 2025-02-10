import pandas as pd
import requests 
from io import StringIO
from sqlalchemy import create_engine


def csv_downloader(csv_url):
    response = requests.get(csv_url)
    if response.status_code == 200:
        data = StringIO(response.text)
        df = pd.read_csv(data)
        return df
    else:
        print("Error downloading file")
        
def send_data_to_db(df, db_name, table_name):
    user_name = 'postgres'
    pw = '12345678'
    host = 'localhost'
    port = '5432'
    db = db_name
    
    db_url = f'postgresql://{user_name}:{pw}@{host}:{port}/{db}'
    engine = create_engine(db_url)
    
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    
    print(f"Data has been sent to {db_name} database as {table_name} table")
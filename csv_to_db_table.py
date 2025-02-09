import pandas as pd
import requests
from io import StringIO
from sqlalchemy import create_engine

# Step 1: Define the direct Google Drive CSV download link
CSV_URL = "https://drive.usercontent.google.com/u/0/uc?id=1TQRSONybodmFG7yBrMuCxb2JRFVaowJR&export=download"

def download_csv(url):
    """Downloads CSV from Google Drive and loads it into Pandas DataFrame."""
    response = requests.get(url)
    if response.status_code == 200:
        data = StringIO(response.text)  # Convert text content to Pandas-readable format
        print("✅ CSV downloaded successfully.")
        return pd.read_csv(data)
    else:
        print("❌ Failed to download CSV.")
        return None

# Download and Load CSV into Pandas
df = download_csv(CSV_URL)

if df is not None:
    # Step 2: Data Cleaning & Transformation
    # df.drop_duplicates(inplace=True)  # Remove duplicate rows
    # df.fillna(method="ffill", inplace=True)  # Handle missing values
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]  # Normalize column names

    # Step 3: Connect to PostgreSQL Database
    POSTGRES_USER = "postgres"  # Change to your PostgreSQL username
    POSTGRES_PASSWORD = "12345678"  # Change to your PostgreSQL password
    POSTGRES_HOST = "localhost"  # Change if running remotely
    POSTGRES_PORT = "5432"  # Default PostgreSQL port
    POSTGRES_DB = "altschool_db"  # Change to your PostgreSQL database name

    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    # Create SQLAlchemy engine
    engine = create_engine(DATABASE_URL)

    # Step 4: Save Data to PostgreSQL
    TABLE_NAME = "flights1"
    df.to_sql(TABLE_NAME, con=engine, if_exists="replace", index=False)  # Use "append" instead of "replace" to keep existing data

    print("✅ Data successfully saved to PostgreSQL.")

    # Step 5: Query & Verify Data
    query_result = pd.read_sql(f"SELECT * FROM {TABLE_NAME} LIMIT 5;", con=engine)
    print(query_result)
else:
    print("❌ No data to save to PostgreSQL.")
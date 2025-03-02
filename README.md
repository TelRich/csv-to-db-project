# CSV Data Pipeline Project

## Overview

This project downloads a CSV file from a given URL, processes the data to separate successful and unsuccessful flights, and then uploads the processed data to a PostgreSQL database.

## Features

- Downloads a CSV file from a remote source.
- Processes the dataset to filter flights based on their cancellation status.
- Uploads the processed data to a PostgreSQL database.

## Requirements

### Dependencies

Ensure you have the following dependencies installed:

- `pandas`
- `requests`
- `sqlalchemy`
- `psycopg2`
- `json`

Install dependencies using pip:

```bash
pip install pandas requests sqlalchemy psycopg2
```

### Configuration

Create a `config.json` file in the project directory with the following structure:

```json
{
    "warehouse": {
        "user": "your_db_user",
        "password": "your_db_password",
        "host": "your_db_host",
        "port": "your_db_port",
        "database": "your_database_name"
    }
}
```

## Usage

### Running the Script

1. Import the required functions:

```python
from csv_module import csv_downloader, send_data_to_db
```

2. Set the CSV file URL:

```python
CSV_URL = "https://drive.usercontent.google.com/u/0/uc?id=1TQRSONybodmFG7yBrMuCxb2JRFVaowJR&export=download"
```

3. Download the CSV file and load it into a DataFrame:

```python
flights = csv_downloader(csv_url=CSV_URL)
```

4. Process the data:

```python
successful_flights = flights[flights['was_cancelled'] == True]
unsuccessful_flights = flights[flights['was_cancelled'] == False]

print(successful_flights.shape)
print(unsuccessful_flights.shape)
```

5. Send data to the database:

```python
table1 = "completed_flights"
table2 = "failed_flights"

send_data_to_db(df=successful_flights, table_name=table1)
send_data_to_db(df=unsuccessful_flights, table_name=table2)
```

## Functions

### `csv_downloader(csv_url)`

- Downloads the CSV file from the provided URL and loads it into a pandas DataFrame.
- Handles request errors gracefully.

### `send_data_to_db(df, table_name)`

- Uploads the given DataFrame to the specified PostgreSQL table.
- Uses database credentials from the `config.json` file.

## Notes

- Ensure your database is running and accessible.
- Modify the database credentials in `config.json` accordingly.

## License

This project is open-source and available for modification and use under the MIT license.


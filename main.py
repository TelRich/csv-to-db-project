from csv_module import csv_downloader, send_data_to_db
import time

def main():
    # Print visual feedback for video demo
    print("1. Downloading CSV data...")
    CSV_URL = "https://drive.usercontent.google.com/u/0/uc?id=1TQRSONybodmFG7yBrMuCxb2JRFVaowJR&export=download"
    flights = csv_downloader(csv_url=CSV_URL)
    
    print("\n2. Processing flight data...")
    print("Total flights:", len(flights))
    
    successful_flights = flights[flights['was_cancelled'] == False]
    unsuccessful_flights = flights[flights['was_cancelled'] == True]
    
    print(f"Successful flights: {len(successful_flights)}")
    print(f"Cancelled flights: {len(unsuccessful_flights)}")
    
    print("\n3. Uploading to database...")
    send_data_to_db(df=successful_flights, table_name="completed_flights")
    time.sleep(1)  # Add slight delay for visual demo
    send_data_to_db(df=unsuccessful_flights, table_name="failed_flights")
    
    print("\nProcess completed successfully!")

if __name__ == "__main__":
    main()

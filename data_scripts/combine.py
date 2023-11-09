import os
import pandas as pd
from pymongo import MongoClient
import certifi

os.environ['SSL_CERT_FILE'] = certifi.where()
# Your MongoDB connection string and database name
mongo_url = "mongodb+srv://eramadani:MQP123@mqp-database.3yyl9tm.mongodb.net/?retryWrites=true&w=majority"
database_name = "NBA"
collection_name = "Nba_collection"

# Path to the folder containing your draft pick CSV files
path_to_draft_picks_folder = "../draft_picks"

# Connect to your MongoDB
client = MongoClient(mongo_url)
db = client[database_name]
collection = db[collection_name]

# Get a list of all draft pick CSV files
csv_files = [file for file in os.listdir(path_to_draft_picks_folder) if file.startswith('nba_draft_pick_') and file.endswith('.csv')]

# Sort the files to maintain the draft pick order
csv_files.sort()

# Iterate through each CSV file and insert its contents into MongoDB
for csv_file in csv_files:
    file_path = os.path.join(path_to_draft_picks_folder, csv_file)
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Convert the DataFrame to a list of dictionaries
    records = df.to_dict(orient='records')
    
    # Insert the records into MongoDB - you can add some error checking around this
    collection.insert_many(records)

print("All files have been processed and uploaded to the MongoDB collection.")

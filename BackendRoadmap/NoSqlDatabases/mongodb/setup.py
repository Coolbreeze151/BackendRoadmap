import pymongo
from pymongo import MongoClient
import os

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']

# Create a collection
collection = db['mycollection']

# Define the directory containing the files to ingest
directory = '/path/to/files'

# Iterate over the files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory, filename)
        
        # Open the file and read its contents
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Create a document to insert into the collection
        document = {
            'filename': filename,
            'content': content
        }
        
        # Insert the document into the collection
        collection.insert_one(document)

# Close the MongoDB connection
client.close()
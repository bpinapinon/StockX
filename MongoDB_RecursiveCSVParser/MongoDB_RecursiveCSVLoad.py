# Verify MongoDB instance is running on the default host and port:
# Initiate in gitbash with command: mongod


# Import Dependencies
import pymongo
from pymongo import MongoClient 
from pprint import pprint
import glob
import numpy as np
import os
import subprocess

# Start MongoDB Server by making OS call "mongod"
mongod = subprocess.Popen('mongod' , shell = True)

# Establish Mongo DB Client Connection
Client = MongoClient()
Client = MongoClient('mongodb://localhost:27017/')

# Show existing DBs
print(f'\nExisting Databases Run 1: Pre DB Drop\n{"-"*40}\n{Client.list_database_names()}')

# Drop StockX_DB if it exists
Client.drop_database("StockX_DB")

# Show existing DBs
print(f'\nExisting Databases Run 2: Post DB Drop\n{"-"*40}\n{Client.list_database_names()}')

# Create StockX_DB if it exists
DatabaseName = 'StockX_DB'
MongoDB = Client[DatabaseName]

# Chart Types List
# Chart = ['bar','bubble','sankey']


# ################################
# # Start MongoDB Load Job
# ################################
print(f'\n\n{"*"*80}\n{"*"*80}\n{"*"*80}\nJOB START: Create Collections and Load Documents...\n{"*"*80}\n{"*"*80}\n{"*"*80}\n')


# Recursively walk through files in folder and read CSVs
DirectoryPath = os.path.join("CSV_Files/")

SeqId = 1

for root, dirs, files in os.walk(DirectoryPath):
    for file in files:
        # print(f'\nFile: {file}')
        if file.endswith(".csv"):
            with open(DirectoryPath+file , 'r') as f:

                ###############################
                # Start Load Run for CSV file
                ###############################
                print(f'{"~"*80}\nJob Run #{SeqId}: Loading Data for "{file}" file...\n{"~"*80}\n')

                # Create Collections
                CollectionName = file.rstrip('.csv')
                Collection = MongoDB[CollectionName]
                print(f'Created Collection in {DatabaseName}:\n{"-"*30}\n{CollectionName}')

                # Begin reading CSV
                CSV_Headers = f.readline()
                
                # Print CSV Headers
                print(f'\nHeaders:\n{"-"*10}\n{CSV_Headers}')

                header = CSV_Headers.strip().split(',')
                next(f)
                for line in f:
                    lines = line.strip().split(',')
                    row = {}
                    for k, v in zip(header, lines):
                        row[k] = v
                    id = Collection.insert_one(row).inserted_id
                    # print(id)    

                # Display 1 Record of Data loaded into our Collection
                cursor = Collection.find({}).limit(1)
                for document in cursor:
                    print(f'\nDisplay 1 Document from Collection:\n{"-"*35}')
                    pprint(document)
                    print(f'\n')

                SeqId = SeqId + 1

print(f'\n{"*"*80}\n{"*"*80}\n{"*"*80}\nJOB COMPLETE\n{"*"*80}\n{"*"*80}\n{"*"*80}')                

#####################################
# Verify DB and Collections Creation 
#####################################
          
# Print Database Names to verify creation of ours
print(f'\nDatabases Post-Job:\n{"-"*40}\n{Client.list_database_names()}')

# Print Collections to verify creation of ours
print(f'\nCollections Post-Job:\n{"-"*40}\n{MongoDB.collection_names()}')

# Close connection to MongoDB
mongod.terminate()

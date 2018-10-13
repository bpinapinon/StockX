import pymongo
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')

Database = client['stockx_db']
ShoesTable = Database.ShoesTable


CSVFiles = ['Top50Adidas.csv', 'Top50Nike.csv']

for file in CSVFiles:
        
    with open(file, 'r') as f:
        print(file)
        head = f.readline()
        print(head) #print headers
        header = head.strip().split(',')
        next(f)
        for line in f:
            lines = line.strip().split(',')
            row = {}
            for k, v in zip(header, lines):
                row[k] = v
            id = ShoesTable.insert_one(row).inserted_id
            print(id)        

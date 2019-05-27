from pymongo import MongoClient

# Note: https://www.mongodb.com/cloud/atlas allows you to create a free mongodb database

# Get db path from configuration file
MONGODB_URL = 

# Open client
client = MongoClient(MONGODB_URL)
db=client.admin # Open the database "admin"

# Open client which uses authentication
client = MongoClient('example.com',
                      username='user',
                      password='password',
                      authSource='the_database',
                      authMechanism='SCRAM-SHA-256')

# Inserting data into the collection
db.collection.insert_one(dict) # Insert "dict" into collection in db

# Finding data in a collection
db.collection.find_one()
posts.find_one({"author": "Nathan Bedell"})


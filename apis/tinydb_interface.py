from tinydb import TinyDB, Query
from yaml import load, dump
from yaml import Loader, Dumper

def openDbConfig() -> Dict[str,str]:
	dbconfig = open("db_config.yaml")
	data = load(dbconfig, Loader=Loader)
	
	# Config file data:
	#     use_tinydb   = data['use_tinydb']
	#     tinydb_path  = data['tinydb_path'] 
	#     use_pymongo  = data['use_pymongo']
	#     pymongo_path = data['pymongo_path']
	
	return load(dbconfig, Loader=Loader)

# Get db path from configuration file
db = TinyDB('/path/to/db.json')

# Syntax for inserting into database
db.insert(query)



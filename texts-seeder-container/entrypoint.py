import os
import pickle
import json
from redis import Redis

host = os.environ['DATABASE_HOST']
port = os.environ['DATABASE_PORT']
db = os.environ['DATABASE_DB']

raw_collection = os.environ['RAW_COLLECTION']
tokenized_collection = os.environ['TOKENIZED_COLLECTION']

connection = Redis(host=host, port=port, db=db)

def __seed_raw_texts():
	raw_texts_filenames = os.listdir('/texts/raw')
	for filename in raw_texts_filenames:
		abs_path = f"/texts/raw/{filename}"
		with open(abs_path, 'r') as f:
			raw_content = f.read()
			connection.hset(raw_collection, filename, raw_content)
	
def __seed_tokenized_texts():
	tokenized_texts_filenames = os.listdir('/texts/tokenized')
	for filename in tokenized_texts_filenames:
		abs_path = f"/texts/tokenized/{filename}"
		with open(abs_path, 'rb') as f:
			tokenized_content = pickle.load(f)
			json_content = json.dumps(tokenized_content)
			connection.hset(tokenized_collection, filename, json_content)

if __name__ == '__main__':
	__seed_raw_texts()
	__seed_tokenized_texts()

	
	
	

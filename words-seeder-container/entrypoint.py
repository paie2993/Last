from redis import Redis
from os import environ

vocabulary_collection = environ['VOCABULARY']
hyphened_collection = environ['HYPHENED']
invalid_hyphened_collection = environ['INVALID_HYPHENED']
stopwords_collection = environ['STOPWORDS']

host = environ['DATABASE_HOST']
port = environ['DATABASE_PORT']
db = environ['DATABASE_DB']

connection = Redis(host=host, port=port, db=db, charset="utf-8")

def read_words(filename) -> list[str]:
	words = []
	with open(filename, 'r') as f:
		for line in f:
			word = line.strip(' \n\t')
			words.append(word)
	return words

if __name__ == '__main__':
	vocabulary = read_words('/words/vocabulary.csv')
	hyphened = read_words('/words/hyphened.csv')
	invalid_hyphened = read_words('/words/invalid_hyphened.csv')
	stopwords = read_words('/words/stopwords.csv')
	
	connection.sadd(vocabulary_collection, *vocabulary)
	connection.sadd(hyphened_collection, *hyphened)
	connection.sadd(invalid_hyphened_collection, *invalid_hyphened)
	connection.sadd(stopwords_collection, *stopwords)

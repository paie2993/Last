import nltk
import pickle

if __name__ == '__main__':
	gutenberg = nltk.corpus.gutenberg
	
	fileids = gutenberg.fileids()
	for fileid in fileids:
		raw = gutenberg.raw(fileid)
		with open(f"raw/{fileid}", 'w') as f:
			f.write(raw)

		tokenized = list(gutenberg.words(fileid))			
		with open(f"tokenized/{fileid}", 'wb') as f:
			pickle.dump(tokenized, f)	

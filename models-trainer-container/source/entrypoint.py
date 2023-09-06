import pickle
from redis import Redis
from time import time
from environment import (
    DATABASE_DB,
    DATABASE_HOST,
    DATABASE_PORT,
    HYPHENATED_CLASSIFIER_NAME,
    TAGGER_NAME,
)

from train_data import get_tagger_train_data, get_hyphenated_classifier_train_data
from trainer import Trainer

connection = Redis(
    host=DATABASE_HOST,
    port=DATABASE_PORT,
    db=DATABASE_DB,
    decode_responses=True,
    encoding="utf-8",
)

# prepare train data
tagger_train_data = get_tagger_train_data()
hyphenated_train_data = get_hyphenated_classifier_train_data(connection)
print("Prepared train data ...", flush=True)

# train the models
trainer = Trainer(tagger_train_data, hyphenated_train_data)

start = time()
tagger = trainer.train_tagger()
end = time()
print(f"Trained POS tagger in {end - start}s", flush=True)

start = time()
hyphenated_classifier = trainer.train_hyphenation_classifier(tagger)
end = time()
print(f"Trained Hyphenation classifier in {end - start}s", flush=True)

# serialize the models
pickled_tagger = pickle.dumps(tagger)
pickled_hyphenated_classifier = pickle.dumps(hyphenated_classifier)

# store to database
connection.set(TAGGER_NAME, pickled_tagger)
connection.set(HYPHENATED_CLASSIFIER_NAME, pickled_hyphenated_classifier)

print("Stored ML models", flush=True)

connection.close()

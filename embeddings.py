import os
import json
import requests
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import joblib

def create_embeddings(text):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text
    })

    return r.json()["embeddings"]

jsons = os.listdir("chunks")
print(jsons)
my_dicts = []
chunk_id = 0
for json_file in jsons:
    with open(f"chunks/{json_file}") as f:
        content = json.load(f)
    
    embeddings = create_embeddings([c['text'] for c in content['chunks']])
    for i , chunk in enumerate(content['chunks']):
        chunk['chunk_id'] = chunk_id
        chunk['embedding'] = embeddings[i]
        my_dicts.append(chunk)
        chunk_id += 1

df = pd.DataFrame.from_records(my_dicts)
joblib.dump(df , "embeedings.joblib")

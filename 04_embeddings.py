import os
import json
import requests
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import joblib 

def create_embeddings(text):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text
    })
    
    return r.json()["embeddings"]
    
files = os.listdir("chunks")

for file in files:
    with open(f"chunks/{file}") as f:
        json_file = json.load(f)
        list_text = [x["text"] for x in json_file["chunks"]]
        embeddings = create_embeddings(list_text)
        x = 0
        for i in json_file["chunks"]:
            i["embedding"] = embeddings[x]
            x +=1
        df = pd.DataFrame(json_file["chunks"])
        simularity = cosine_similarity(create_embeddings(["setting  up a vscode"]) , df["embedding"].tolist())
        index = simularity.argmax()
        print(df.iloc[index])
        break


            
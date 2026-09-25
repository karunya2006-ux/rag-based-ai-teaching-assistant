import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import requests
import json
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
def response(prompt):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    interaction = client.interactions.create(
        model=os.getenv("GEMINI_MODEL"),
        input=prompt
    )
    
    return interaction.output_text



def create_embeddings(text):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text
    })

    return r.json()["embeddings"]

df = joblib.load("embeedings.joblib")
incomming_query = input("ask a question : ")
question_embeeeding = create_embeddings([incomming_query])[0]
similarities = cosine_similarity(np.vstack(df['embedding']),[question_embeeeding]).flatten()

top_results = 5
max_index = similarities.argsort()[::-1][0:top_results]

new_df = df.loc[max_index]

prompt = f''' i am teaching web dovelopment using sigma web dev courseHere are video subtitle chunks containing video title, video number, start time in seconds, end time in seconds, the text at that :
{new_df[['title','number','start','end','text']].to_json()}

-----------------------------------------
"{incomming_query}"
User asked this question related to the video chunks, you have to answer where and how much
content is taught in which video (in which video and at what timestamp) and guide the user to go
to that particular video. If user asks unrelated question, tell him that you can only answer
questions related to the course
'''

r = response(prompt)

print(r)
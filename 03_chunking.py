import os
import json
import pandas as pd

files = os.listdir("textoutputs(json)")


for file in files:
    chunks = []
    filepath = os.path.join("textoutputs(json)", file)
    with open(filepath ,"r")as f:
        data = json.load(f)
        for i in data['segments']:
            dict = { 'number' : file.split('_')[0] , 'title' : file.split('_')[1].split('.')[0] , 'start' : i['start'] , 'end' : i['end'] , 'text' : i['text'] }
            chunks.append(dict)
        chunks_with_metadata =  {'chunks' : chunks , "text" : data['text']}   
        
        with open(f"chunks/{file}.json" , "w") as f:
            json.dump(chunks_with_metadata , f)
# df = pd.DataFrame(chunks)
# df.to_csv('chunking.csv',index = False)

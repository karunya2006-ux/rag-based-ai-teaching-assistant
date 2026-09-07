import whisper
import json
import os
# model = whisper.load_model("large-v2")
# result = model.transcribe(audio = "output.mp3" , language = "hi" , task = "translate" , word_timestamps = False)
# print(result)
# with open("output.json" , "w") as f:
#     json.dump(f, result)
files = os.listdir("audios")
model = whisper.load_model("large-v2")
for file in files:
    result = model.transcribe(audio = f"audios/{file}" , language = "hi" , task = "translate")
    with open(f"{file}.json" , "w") as f:
        json.dump(result, f)
    
print(f"Finished: {file}")
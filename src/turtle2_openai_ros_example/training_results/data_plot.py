import json

#upload data and set file handle 
with open(openaigym.episode_batch.0.6746.stats.json) as json_data:
    #load method is passed the file handle and reads the file
    d = json.load(json_data)
    print(type(d))
    print(type(d[0]))
    print(json.dumps(d[0], indent=2))


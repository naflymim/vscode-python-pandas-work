import json
import os
import pandas as pd

file_path = r"I:\Web Developments\Python\VSCode\Panadas\Demo - Json\000"
keys_to_use = ['id', 'all_artists', 'title', 'medium', 'acquisitionYear', 'height', 'width', 'units']

def get_record_from_file(file_path, key_to_use):  

    with open(file_path) as artwork_file:       
        context = json.load(artwork_file)

    record = []
    for field in key_to_use:
        record.append(context[field])

    return tuple(record)

# Run for only one file
artworks = []
for root, dirs, files in os.walk(file_path, topdown=False):   
    for file_name in files:
        sample_json_file = os.path.join(file_path, file_name)
        if(os.path.exists(sample_json_file) and str(file_name).endswith('json')):    
            record = get_record_from_file(sample_json_file, keys_to_use)
            artworks.append(record)

df = pd.DataFrame.from_records(artworks, columns=keys_to_use, index="id")
#print(df)




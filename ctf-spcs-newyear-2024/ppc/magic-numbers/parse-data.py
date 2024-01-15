import os
import json

json_file_path = 'output.json'
with open(json_file_path, 'r') as file:
    data = json.load(file)

result_dict = {}

for key, values in data.items():
    common_prefix = os.path.commonprefix([val.split() for val in values])
    result_dict[key] = " ".join(common_prefix)

file_path = "final.json"

with open(file_path, 'w') as json_file:
    json.dump(result_dict, json_file, indent=4)

print(f"JSON data has been written to {file_path}")
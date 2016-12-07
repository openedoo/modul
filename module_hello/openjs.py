import json

with open('requirement.json') as data_file:
    data_json = json.loads(data_file.read())

print data_json['requirement'][0]

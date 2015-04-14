import json

# Pretend we're doing something that's generating data
a = {"conference": "FOMMS",
     "year": 2015,
     "languages": ["python"],
     "names": [{"first": "Patrick", "last": "Fuller"},
               {"first": "Chris", "last": "Wilmer"}]}

# Write the output to a file as json
with open("v1.json", "w") as out_file:
    json.dump(a, out_file)

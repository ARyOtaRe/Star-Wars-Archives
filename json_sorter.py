import json

with open('This\\is\\path\\to\\origin.json','r') as input_json_file:
    data = json.loads(input_json_file.read())

with open('That\\is\\path\\to\\destination.json','w') as output_json_file:
    oof=json.dumps(data, sort_keys=True,indent=2)
    json.dump(oof,output_json_file)



"""

sorted_json_data = json.dumps(data, sort_keys=True)
# Print the sorted JSON data
print("The sorted JSON data based on the keys:\n{0}".format(sorted_json_data))
"""

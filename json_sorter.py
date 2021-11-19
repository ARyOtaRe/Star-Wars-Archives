import json

with open('C:\\Users\\ARyOtaRe\\Documents\\GitHub\\StarWarsElphebat\\SWPlanets.json','r') as input_json_file:
    data = json.loads(input_json_file.read())

with open('C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Star-Wars-Archives\\swplanets.json','w') as output_json_file:
    oof=json.dumps(data, sort_keys=True,indent=2)
    output_json_file.write(oof)



"""

sorted_json_data = json.dumps(data, sort_keys=True)
# Print the sorted JSON data
print("The sorted JSON data based on the keys:\n{0}".format(sorted_json_data))
"""

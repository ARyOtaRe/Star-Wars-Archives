import json

with open('C:\\Users\\ARyOtaRe\\Documents\\GitHub\\StarWarsElphebat\\SWPlanets.json','r') as input_json_file:
    data = json.loads(input_json_file.read())

with open('C:\\Users\\ARyOtaRe\\Documents\\GitHub\\Star-Wars-Archives\\swplanets.json','w') as output_json_file:
    oof=json.dumps(data, sort_keys=True,indent=2)
    output_json_file.write(oof)



"""
import pkg_resources
from subprocess import call

packages = [dist.project_name for dist in pkg_resources.working_set]
call("pip3.8 install --upgrade " + ' '.join(packages), shell=True)
"""
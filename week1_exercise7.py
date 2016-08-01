import yaml
import json
from pprint import pprint as pp

# initialize the yaml list
yaml_list = []

# read in the list values using yaml
print "Reading in yaml format and printing results..."

# read the file with yaml
with open ("week1_6_yaml.yml", "r") as f:
  yaml_list = yaml.load(f)

# pretty print the list
pp(yaml_list)

# add some newlines
print ""
print ""

# initialize the list
json_list = []

# read in the list values using yaml
print "Reading in json format and printing results..."

# read the file with json
with open ("week1_6_json.jsn", "r") as f:
  json_list = json.load(f)

# pretty print the list
pp(json_list)



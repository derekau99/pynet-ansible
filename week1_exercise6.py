import yaml
import json

# Parameter values
my_name = "Derek Au"
my_email = "derekau99@gmail.com"
my_phone = "650-353-0921"
device_name = "sf-rtr1"
device_location = "sfo1"
device_management_interface = "Management0"
device_management_ip_address = "10.25.7.21"
device_management_ip_mask = "255.255.0.0"
device_management_ip_default_gateway = "10.25.0.1"

# initialize the list
test_list = []

# append some values to the list
test_list.append(my_name)
test_list.append(my_email)
test_list.append(my_phone)

# append a dictionary to the list
test_list.append({'device-name' : device_name})
test_list.append({'device-location' : device_location})
test_list.append({'management-interface' : device_management_interface})
test_list.append({'management-ip-address' : device_management_ip_address})
test_list.append({'management-ip-mask' : device_management_ip_mask})
test_list.append({'management-ip-default-gateway' : device_management_ip_default_gateway})

# show us the list using yaml
print "This is how it looks in yaml format..."
print yaml.dump(test_list, default_flow_style=False)

# save the list with yaml
with open ("week1_6_yaml.yml", "w") as f:
  f.write(yaml.dump(test_list, default_flow_style=False))

# add some newlines
print ""
print ""

# show us the list using json
print "This is how it looks in json format..."
print json.dumps(test_list)

# save the list with json
with open ("week1_6_json.jsn", "w") as g:
  json.dump(test_list,g)

# add some newlines
print ""
print ""



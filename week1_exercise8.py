from ciscoconfparse import CiscoConfParse

config = CiscoConfParse("cisco_ipsec.txt")

crypto_maps = config.find_objects("crypto map")

for crypto_entry in crypto_maps:
  print crypto_entry.text
  for child in crypto_entry.children:
    print child.text



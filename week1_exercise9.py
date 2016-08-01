from ciscoconfparse import CiscoConfParse

config = CiscoConfParse("cisco_ipsec.txt")

crypto_maps = config.find_objects("crypto map")

for crypto_entry in crypto_maps:
  for child in crypto_entry.children:
    if child.text.find("pfs group2") >= 0 :
      print(crypto_entry.text + "is an entry that uses PFS group 2")



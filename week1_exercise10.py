from ciscoconfparse import CiscoConfParse

config = CiscoConfParse("cisco_ipsec.txt")

crypto_maps = config.find_objects("crypto map")

for crypto_entry in crypto_maps:
  uses_AES = False
  for child in crypto_entry.children:
    if child.text.find("transform-set AES") >= 0:
      uses_AES = True
  if uses_AES == False:
    print(crypto_entry.text + "is an entry that does not use AES")


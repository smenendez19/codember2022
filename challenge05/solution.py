import requests
import json

# Get list techs
response = requests.request("GET", "https://codember.dev/mecenas.json")
list_techs_original = json.loads(response.text)

# Index list
list_techs = []
for i in range(0, len(list_techs_original)):
    list_techs.append(f"{list_techs_original[i]}-{i}")

while len(list_techs) > 1:
    survivors = []
    for i in range(0, len(list_techs)):
        if i % 2 == 0:
            survivors.append((list_techs[i]))
    if len(list_techs) % 2 != 0:
        survivors.pop(0)
    list_techs = []
    for survivor in survivors:
        list_techs.append(survivor)

print(list_techs[0])
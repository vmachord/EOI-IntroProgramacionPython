import json

citricos=["Limon","naranja","pomelo","lima"]

citricosJSON=json.dumps(citricos)
print(type(citricosJSON))
print("Json de citricos:",citricosJSON)

listacitricos = json.loads(citricosJSON)

print(listacitricos)
print(type(listacitricos))

import json

'''x = {"nome": "Pera",
     "idade": 10}

y= json.dumps(x)'''

y = json.load(open("Estudos/dados.json"))

print(y)
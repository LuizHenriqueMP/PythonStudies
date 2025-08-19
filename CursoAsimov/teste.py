nome = "seexxxxoooxoxoxo"
mae = []

for i in range(len(nome)):
    if nome[i] != "x":
        mae.append(nome[i])

for i in mae:
    print(i, end="")
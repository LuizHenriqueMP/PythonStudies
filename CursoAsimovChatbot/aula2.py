import sys

print("Boa tarde mestre!")
print("Digite x para sair\nO que gostaria de saber hoje?")
pergunta = input("> ")

def sair():
      if pergunta.lower() == "x":
        print("Tenha um bom dia.")
        sys.exit()

sair()

if pergunta.count("pokemon") > 0:
        print("Você gosta de pokemon??? Eu também!!!")

while True:
    print("Resposta do bot aqui")
    pergunta = input("> ")

    if pergunta.count("pokemon") > 0:
        print("Você gosta de pokemon??? Eu também!!!")

    sair()
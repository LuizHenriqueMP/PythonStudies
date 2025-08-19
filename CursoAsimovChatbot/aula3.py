import sys

mensagens = []

def resposta_bot(mensagens):
     return "Resposta do bot"

def sair():
      if pergunta.lower() == "x":
        print("Tenha um bom dia.")
        sys.exit()

print("Boa tarde Mestre!\nDigite x para sair")

while True:
    pergunta = input("Usuário-")
    sair()
    mensagens.append({"role" : "user" , "content": pergunta})
    resposta = resposta_bot(mensagens)
    mensagens.append({"role": "assistant", "content": resposta})
    print(f"Bot-{resposta}")

print(mensagens)
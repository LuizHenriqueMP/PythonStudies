import os
from langchain_groq import ChatGroq

api_key = "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"
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.1-70b-versatile')

while True:
    pergunta = input("User: ")
    if pergunta == "sair":
        break
    resposta = chat.invoke(pergunta)
    print("Bot: "+resposta.content)
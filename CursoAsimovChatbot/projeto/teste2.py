import os
from langchain_groq import ChatGroq

import apikey
api_key = apikey.api_key
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.1-70b-versatile')

while True:
    pergunta = input("User: ")
    if pergunta == "sair":
        break
    resposta = chat.invoke(pergunta)
    print("Bot: "+resposta.content)
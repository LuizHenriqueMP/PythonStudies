import os
from langchain_groq import ChatGroq

import apikey
api_key = apikey.api_key
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.1-70b-versatile')

resposta = chat.invoke('Olá, quem é você?')

print(resposta.content)
import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

import apikey
api_key = apikey.api_key
os.environ['GROQ_API_KEY'] = api_key

template = ChatPromptTemplate.from_messages(
    [('system','Você é um assistente que sempre responde com piadas'),
    ('user','Traduza a expressão {expressao} para a língua {lingua}')]
)

chat = ChatGroq(model='llama-3.1-70b-versatile')

chain = template | chat

resposta = chain.invoke({'expressao': 'Beleza?', 'lingua':'inglesa'})
print(resposta.content)
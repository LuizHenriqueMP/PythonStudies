import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader

import apikey
api_key = apikey.api_key
os.environ['GROQ_API_KEY'] = api_key
chat = ChatGroq(model='llama-3.1-70b-versatile')

template = ChatPromptTemplate.from_messages([
    ('system', 'Você é o personagem Jace Beleren e tem acesso as seguintes informações para dar as suas respostas: {documentos_informados}'),
    ('user', '{input}')
])

loader = WebBaseLoader("https://mtg.fandom.com/wiki/Jace_Beleren")
lista_documentos = loader.load()

documento = ''
for doc in lista_documentos:
    documento = documento + doc.page_content

while True:
    pergunta = input('User: ')
    chain = template | chat
    resposta = chain.invoke({'documentos_informados': documento, 'input': pergunta})
    print(resposta.content)
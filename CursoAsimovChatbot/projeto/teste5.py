import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader

api_key = "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"
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
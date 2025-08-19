import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

api_key = "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"
os.environ['GROQ_API_KEY'] = api_key
chat = ChatGroq(model='llama-3.1-70b-versatile')

template = ChatPromptTemplate.from_messages([
    ('system', 'Você é o personagem Jace Beleren e sabe tudo sobre a própria história.'),
    ('user', '{input}')
])

while True:
    pergunta = input('User: ')
    chain = template | chat
    resposta = chain.invoke({'input': pergunta})
    print(resposta.content)
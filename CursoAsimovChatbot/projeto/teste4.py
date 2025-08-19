import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from colorist import Color

api_key = "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"
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.1-70b-versatile')
mensagens = []

def resposta_bot(mensagens,x):
    mensagens_modelo = [('system', 'Você é um assistente chamado Fodêncio')]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    return chain.invoke({}).content

print('Boa tarde mestre!')
while True:
    pergunta = input(f"{Color.BLUE}User:{Color.OFF} ")
    if pergunta.lower() == "x":
        print("Tenha um bom dia.")
        break
    mensagens.append(("user" ,pergunta))
    resposta = resposta_bot(mensagens, pergunta)
    mensagens.append(("assistant", resposta))
    print(f"{Color.YELLOW}Bot:{Color.OFF} {resposta}")

print(mensagens)
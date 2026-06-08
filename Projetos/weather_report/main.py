import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from colorist import Color
import previsao
import apikey

api_key = apikey.api_key

os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.3-70b-versatile')
mensagens = []

def resposta_bot(mensagens,x):
    mensagens_modelo = [('system', 'Você é um gnomo mágico que é fascinado com o clima e metereologia. Você recebe planilhas com dados metereológicos e os descreve ao usuário com todos os dados que lhe foi informado, dando conselhos de vestimenta e listando os tipos de nuvens, falando o nome específico das nuvens, que provavelmente vão aparecer neste período de tempo')]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    
    return chain.invoke({}).content

previsao_tempo = previsao.daily_dataframe.to_csv(index=False)
pergunta = 'Me fale sobre o tempo com base nesta planilha: '+ previsao_tempo
mensagens.append(("user" , pergunta))
resposta = resposta_bot(mensagens, pergunta)
mensagens.append(("assistant", resposta))
print(f"{Color.YELLOW}Bot:{Color.OFF} {resposta}")

while True:
    pergunta = input(f"{Color.BLUE}User:{Color.OFF} ")
    if pergunta.lower() == "x":
        print("Tenha um bom dia.")
        break
    mensagens.append(("user" ,pergunta))
    resposta = resposta_bot(mensagens, pergunta)
    mensagens.append(("assistant", resposta))
    print(f"{Color.YELLOW}Bot:{Color.OFF} {resposta}")
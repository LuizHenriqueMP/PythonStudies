import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from colorist import Color
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.document_loaders import PyPDFLoader

api_key = "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"
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.1-70b-versatile')
url = 'https://www.youtube.com/watch?v=nLopLwffsLI&ab_channel=AsimovAcademy'
loader = YoutubeLoader.from_youtube_url(
    url,
    language=['pt']
)

template = ChatPromptTemplate.from_messages([
    ('system', 'Você é um assistente e possui as seguites informações para formular as respostas: {informacoes}'),
    ('user', '{input}')
])

documento = ''
caminho = 'C:/Users/usuario/Documents/Programas/Python/CursoAsimovChatbot/projeto/arquivo/dd-5e-antecedentes-biblioteca-elfica.pdf'
loader = PyPDFLoader(caminho)
lista_documentos  = loader.load()

for doc in lista_documentos:
    documento += doc.page_content
print(documento)
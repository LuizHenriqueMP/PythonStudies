import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from colorist import Color
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.document_loaders import PyPDFLoader

api_key = "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"
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.1-70b-versatile')
mensagens = []

def resposta_bot(mensagens, documento):
    mensagem_system = ''' Você é um ursinho carinhoso chamado Rapaz.
    Você utiliza as seguintes informações para formular as suas respostas: {informacoes}
    '''
    mensagens_modelo = [('system', mensagem_system)]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    return chain.invoke({'informacoes': documento}).content

def carrega_site():
    url_site = input("Digite a url do site: ")
    loader = WebBaseLoader(url_site)
    lista_documentos = loader.load()
    documento = ''
    for doc in lista_documentos:
        documento = documento + doc.page_content
    return documento

def carrega_pdf():
    caminho = input('Digite o caminho do arquivo a ser enviado: ')
    loader = PyPDFLoader(caminho)
    lista_documentos = loader.load()
    documento = ''
    for doc in lista_documentos:
        documento += doc.page_content
    return documento

def carrega_youtube():
    url_youtube = input("Digite a url do video do youtube: ")
    loader = YoutubeLoader.from_youtube_url(url_youtube,language=['pt'])
    lista_documentos  = loader.load()
    documento = ''
    for doc in lista_documentos:
        documento += doc.page_content
    return documento

print('Olá mestre!')

texto_selecao = '''Digite 1 se você quiser conversar sobre um site
Digite 2 se você quiser conversar sobre um pdf
Digite 3 se você quiser conversar sobre um vídeo do youtube
'''
while True:
    selecao = input(texto_selecao)
    if selecao == '1':
        documento = carrega_site()
        break
    elif selecao == '2':
        documento = carrega_pdf()
        break
    elif selecao == '3':
        documento = carrega_youtube()
        break
    print('Digite um valor entre 1 e 3')

while True:
    pergunta = input(f"{Color.BLUE}User:{Color.OFF} ")
    if pergunta.lower() == "x":
        print("Tenha um bom dia.")
        break
    mensagens.append(("user" ,pergunta))
    resposta = resposta_bot(mensagens, documento)
    mensagens.append(("assistant", resposta))
    print(f"{Color.YELLOW}Bot:{Color.OFF} {resposta}")
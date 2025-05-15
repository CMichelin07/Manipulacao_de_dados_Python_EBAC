import requests


def enviar_arquivo():
    #Caminho arquivo para upload
    caminho = "C:/Users/Carlos/OneDrive/Área de Trabalho/EBAC - Ti do Zero ao Pro/Analista de Dados/Manipulação de Dados com Python/produtos_informatica.xlsx"

    #Enviar o arquivo
    requisicao = requests.post(url= 'https://file.io', files={"file": open(caminho, "rb")})
    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao["link"]
    print("Arquivo enviado. Link para acesso", url)

def receber_arquivo(file_url):
    # Receber o arquivo
    requisicao = requests.get(file_url)

    # Salvar o arquivo
    if requisicao.ok:
        with open("arquivo_baixado.xlsx", "wb") as file:
            file.write(requisicao.content)
        print("Arquivo baixado com sucesso.")
    else:
        print("Erro ao baixar o arquivo:", requisicao.json())

enviar_arquivo()


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Cabeçalho HTTP adicionado para simular o acesso por um navegador
# Isso foi necessário porque sem o cabeçalho, o site retornava um HTML incompleto.
header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
}

print('REQUEST: ')
# Alteração: incluído o parâmetro `headers=header` na requisição para simular um navegador
response = requests.get('https://finance.yahoo.com/quote/%5EBVSP/history/', headers=header)
print(response.text[:600])

print('Beautiful: ')
soup = BeautifulSoup(response.text, features='html.parser')
print(soup.prettify()[:1000])

print('Pandas: ')
# Alteração: agora `pandas.read_html` usa o conteúdo HTML da resposta `response.text`
# antes, o pandas tentava acessar a URL diretamente (o que falhava sem o cabeçalho)
url_dados = pd.read_html(response.text)
print(url_dados[0].head(10))
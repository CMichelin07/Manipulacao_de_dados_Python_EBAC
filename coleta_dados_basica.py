import requests
from bs4 import BeautifulSoup
import pandas

response = requests.get( "https://br.investing.com/indices/bovespa-historical-data" )
print(response.text[:600])

soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify()[:1000])

print ("Pandas:")
url_dados = pandas.read_html("https://br.investing.com/indices/bovespa-historical-data")
print(url_dados[0].head(10))


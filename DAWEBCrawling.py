# Declarando as bibliotecas
import requests
import csv
from bs4 import BeautifulSoup as soup
from requests.exceptions import HTTPError

# Utilizando o pacote requests para fazer o download da página da Web

import requests 
from requests.exceptions import HTTPError
import re

def crawl_website (url:str) -> str:

  try:
    resposta = requests.get(url)
    resposta.raise_for_status()
  except HTTPError as exc:
    print (exc)
  else:
    return resposta.text

#Conferindo como web crawler pode interagir

URL = 'https://github.com/trending'

robots = crawl_website(url = URL)
print(robots)

#Extraindo informações da Web

from bs4 import BeautifulSoup
pagina = BeautifulSoup(open('trending.csv', mode='r'), 'html.parser')

#Criando o arquivo CSV e extraindo os 10 projeto mais populares

pagina = soup(conteudo, 'html.parser')
top10 = pagina.find_all('span', class_='text-normal')

with open(file='github.csv', mode='w', encoding='utf8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["Posição", "Repositório"])

    for i in range(1,11):
        txt = top10[i].text.replace(" ", "").replace("/", "").strip()
        writer.writerow([i,txt])
        print(f"{i}-{txt}")


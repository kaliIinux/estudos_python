import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes['USDBRL']['bid'] 
print(cotacoes) #Printa todas as cotações
print(cotacao_dolar) #Printa a cotação do dólar
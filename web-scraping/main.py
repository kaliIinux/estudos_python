from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep


options = Options()
options.add_argument('window-size=1000,1800')

navegador = webdriver.Chrome(options=options)

navegador.get("https://www.magazineluiza.com.br/")
sleep(1.8)

input = navegador.find_element('tag name', 'input')
input.send_keys("celular samsung")
sleep(1.5)
input.submit()
sleep(2)

navegador.refresh()

lista = navegador.find_element('xpath', '/html/body/div[1]/div/main/section[4]/div[3]/div/ul')
celulares = lista.text
celulares = celulares.split("\n")

preco = navegador.find_element('xpath', '/html/body/div[1]/div/main/section[4]/div[3]/div/ul/li[1]/a/div[3]/div[2]/div/p')
valores = preco.text
valores = valores.split("/n")

count = 0
count1 = 0

for celular in celulares:
    if "Smartphone" in celular:
        if count == 10:
            break
        else:
            print(celular)
            count += 1

print(valores)    
#for preco in celulares:
#    if "R$" in preco:
#        if count1 == 10:
#            break
#        else:
#            print(preco)
#            count1 += 1

sleep(100000)

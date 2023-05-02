from selenium import webdriver
from time import sleep

navegador = webdriver.Chrome()

navegador.get("https://www.magazineluiza.com.br/")
sleep(10)
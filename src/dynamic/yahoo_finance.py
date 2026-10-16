from time import sleep

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://finance.yahoo.com/chart/AAPL#eyJsYXlvdXQiOnsiaW50ZXJ2YWwiOjEsInBlcmlvZGljaXR5IjoxLCJ0aW1lVW5pdCI6Im1pbnV0ZSIsImNhbmRsZVdpZHRoIjoyLjEwMjA5ODQ0ODQ5NDIyNDIsImZsaXBwZWQiOmZhbHNlLCJ2b2x1bWVVbmRlcmxheSI6dHJ1ZSwiYWRqIjp0cnVlLCJjcm9zc2hhaXIiOnRydWUsImNoYXJ0VHlwZSI6Im1vdW50YWluIiwiZXh0ZW5kZWQiOmZhbHNlLCJtYXJrZXRTZXNzaW9ucyI6e30sImFnZ3JlZ2F0aW9uVHlwZSI6Im9obGMiLCJjaGFydFNjYWxlIjoibGluZWFyIiwic3R1ZGllcyI6eyLigIx2b2wgdW5kcuKAjCI6eyJ0eXBlIjoidm9sIHVuZHIiLCJpbnB1dHMiOnsiU2VyaWVzIjoic2VyaWVzIiwiaWQiOiLigIx2b2wgdW5kcuKAjCIsImRpc3BsYXkiOiLigIx2b2wgdW5kcuKAjCJ9LCJvdXRwdXRzIjp7IlVwIFZvbHVtZSI6IiMwZGJkNmVlZSIsIkRvd24gVm9sdW1lIjoiI2ZmNTU0N2VlIn0sInBhbmVsIjoiY2hhcnQiLCJwYXJhbWV0ZXJzIjp7ImNoYXJ0TmFtZSI6ImNoYXJ0IiwiZWRpdE1vZGUiOnRydWV9LCJkaXNhYmxlZCI6ZmFsc2V9fSwicGFuZWxzIjp7ImNoYXJ0Ijp7InBlcmNlbnQiOjEsImRpc3BsYXkiOiJBQVBMIiwiY2hhcnROYW1lIjoiY2hhcnQiLCJpbmRleCI6MCwieUF4aXMiOnsibmFtZSI6ImNoYXJ0IiwicG9zaXRpb24iOm51bGx9LCJ5YXhpc0xIUyI6W10sInlheGlzUkhTIjpbImNoYXJ0Iiwi4oCMdm9sIHVuZHLigIwiXX19LCJzZXRTcGFuIjp7Im11bHRpcGxpZXIiOjEsImJhc2UiOiJ0b2RheSIsInBlcmlvZGljaXR5Ijp7ImludGVydmFsIjoxLCJwZXJpb2QiOjEsInRpbWVVbml0IjoibWludXRlIn0sInNob3dFdmVudHNRdW90ZSI6dHJ1ZSwiZm9yY2VMb2FkIjp0cnVlfSwib3V0bGllcnMiOmZhbHNlLCJhbmltYXRpb24iOnRydWUsImhlYWRzVXAiOnsic3RhdGljIjp0cnVlLCJkeW5hbWljIjpmYWxzZSwiZmxvYXRpbmciOmZhbHNlfSwibGluZVdpZHRoIjoyLCJmdWxsU2NyZWVuIjp0cnVlLCJzdHJpcGVkQmFja2dyb3VuZCI6dHJ1ZSwiY29sb3IiOiIjMDA4MWYyIiwiY3Jvc3NoYWlyU3RpY2t5IjpmYWxzZSwiZG9udFNhdmVSYW5nZVRvTGF5b3V0Ijp0cnVlLCJzeW1ib2xzIjpbeyJzeW1ib2wiOiJBQVBMIiwic3ltYm9sT2JqZWN0Ijp7InN5bWJvbCI6IkFBUEwiLCJxdW90ZVR5cGUiOiJFUVVJVFkiLCJleGNoYW5nZVRpbWVab25lIjoiQW1lcmljYS9OZXdfWW9yayIsInBlcmlvZDEiOjE3OTEzMDUwNDAsInBlcmlvZDIiOjE3OTIwNjkyMDB9LCJwZXJpb2RpY2l0eSI6MSwiaW50ZXJ2YWwiOjEsInRpbWVVbml0IjoibWludXRlIiwic2V0U3BhbiI6eyJtdWx0aXBsaWVyIjoxLCJiYXNlIjoidG9kYXkiLCJwZXJpb2RpY2l0eSI6eyJpbnRlcnZhbCI6MSwicGVyaW9kIjoxLCJ0aW1lVW5pdCI6Im1pbnV0ZSJ9LCJzaG93RXZlbnRzUXVvdGUiOnRydWUsImZvcmNlTG9hZCI6dHJ1ZX19XSwicmFuZ2UiOm51bGwsInJlbmRlcmVycyI6W119LCJldmVudHMiOnsiZGl2cyI6dHJ1ZSwic3BsaXRzIjp0cnVlLCJ0cmFkaW5nSG9yaXpvbiI6Im5vbmUiLCJzaWdEZXZFdmVudHMiOltdfSwiZHJhd2luZ3MiOm51bGwsInByZWZlcmVuY2VzIjp7ImN1cnJlbnRQcmljZUxpbmUiOnRydWUsImRpc3BsYXlDcm9zc2hhaXJzV2l0aERyYXdpbmdUb29sIjpmYWxzZSwiZHJhZ2dpbmciOnsic2VyaWVzIjp0cnVlLCJzdHVkeSI6ZmFsc2UsInlheGlzIjp0cnVlfSwiZHJhd2luZ3MiOm51bGwsImhpZ2hsaWdodHNSYWRpdXMiOjEwLCJoaWdobGlnaHRzVGFwUmFkaXVzIjozMCwibWFnbmV0IjpmYWxzZSwiaG9yaXpvbnRhbENyb3NzaGFpckZpZWxkIjpudWxsLCJsYWJlbHMiOnRydWUsImxhbmd1YWdlIjpudWxsLCJ0aW1lWm9uZSI6IkFtZXJpY2EvTmV3X1lvcmsiLCJ3aGl0ZXNwYWNlIjowLCJ6b29tSW5TcGVlZCI6bnVsbCwiem9vbU91dFNwZWVkIjpudWxsLCJ6b29tQXRDdXJyZW50TW91c2VQb3NpdGlvbiI6ZmFsc2V9fQ=="
HEADERS = {"User-Agent": "Mozilla/5.0"}

response = requests.get(URL, headers=HEADERS)
text = response.text

# Cria as opções do Chrome
options = Options()

# Configura para o navegador NÃO fechar ao término do script 
# options.add_experimental_option("detach", True)
# Opcao para tela cheia
options.add_argument("--start-maximized")
# Executa o Chrome em modo headless (sem interface gráfica)
# options.add_argument("--headless")  

driver = webdriver.Chrome(options=options)
driver.get(URL)

for i in range(2):
    xPath = '//*[@id="right-rail"]/section/div/section[3]/table/tbody/tr[' + str(i + 1) + ']'

    try:
        # Espera de até 10 segundos para o elemento carregar na tela
        elements = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xPath))
        )  

        print("Elemento encontrado com sucesso:")

        columns = elements.find_elements(By.XPATH, "./td")

        # Transformar os elementos em uma lista de strings
        column_texts = [col.text for col in columns]
        print(column_texts)

        find_link = elements.find_element(By.XPATH, "./td[1]/a")
        link = find_link.get_attribute("href")
        print(f"Link encontrado: {link}")
    
    except Exception as e:
        print(f"Erro ao localizar o elemento: {e}")
        print("Dica: Verifique se a estrutura da página mudou ou se o XPath precisa ser simplificado.")
    

# element = driver.find_element(By.CSS_SELECTOR, 'section.info')
# print(element.text)

saveEveryX = 30
xPathBTC = '/html/body/div[2]/main/div[2]/cq-context/section/div/div/aside[2]/section/div/section[8]/table/tbody/tr[1]'

while True:
    try:
        # Espera de até 10 segundos para o elemento carregar na tela
        elements = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xPathBTC))
        )  

        columns = elements.find_elements(By.XPATH, "./td")

        # Transformar os elementos em uma lista de strings
        column_texts = [col.text for col in columns]
        print(column_texts)

        with open("btc_price.txt", "a") as file:
            file.write(",".join(column_texts) + "\n")

    except Exception as e:
        print(f"Erro ao localizar o elemento: {e}")
        print("Dica: Verifique se a estrutura da página mudou ou se o XPath precisa ser simplificado.")

    sleep(saveEveryX)

# driver.close()
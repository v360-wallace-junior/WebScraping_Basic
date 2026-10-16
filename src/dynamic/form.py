from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

urlGoogle = "https://www.google.com"

# Tela cheia
options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

# Adicionar cabeçalho para navegador não ser bloqueado
options.add_argument("--disable-blink-features=AutomationControlled")

browser = webdriver.Chrome(options=options)
browser.get(urlGoogle)

try:
    # Espera de até 10 segundos para o elemento carregar na tela
    element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "ti6dpd"))
        )

    # Busca o elemento pelo ID e insere o texto "Python"
    search_box = browser.find_element(By.ID, "ti6dpd")
    search_box.send_keys("Python")

    # Busca o botão de pesquisa e clica nele
    search_button = browser.find_element(By.CSS_SELECTOR, 'button[jsname="B6rgad"]')
    search_button.click()
    
except Exception as e:
        print(f"Erro ao localizar o elemento: {e}")
        print("Dica: Verifique se a estrutura da página mudou ou se o XPath precisa ser simplificado.")
    


# browser.quit()

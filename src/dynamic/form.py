from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

urlGoogle = "https://www.google.com"

# Tela cheia
options = Options()
options.add_argument("--start-maximized")

browser = webdriver.Chrome(options=options)
browser.get(urlGoogle)

inputElement = browser.find_element(By.NAME, "q")
inputElement.send_keys("Hello, World!")

# browser.quit()
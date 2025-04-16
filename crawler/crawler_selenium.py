#nosso robô principal
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configura o Chrome (abre visível para ver o que está acontecendo)
options = Options()
options.add_argument("--start-maximized")

# Inicia o navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # 1. Abre a página de login local
    driver.get("file:///C:/Users/Vick Oliveira/Downloads/Crawler_Halliburton/simulador_html/login.html")

    time.sleep(1)

    # 2. Preenche usuário e senha
    driver.find_element(By.ID, "usuario").send_keys("meu_usuario")
    driver.find_element(By.ID, "senha").send_keys("minha_senha")

    # 3. Clica no botão de login
    driver.find_element(By.ID, "entrar").click()
    time.sleep(2)

    # 4. Estamos agora na página com a árvore
    # Exemplo de clique em um item de menu simulado
    itens = driver.find_elements(By.CLASS_NAME, "item-cwi")
    for item in itens:
        print("Clicando no:", item.text)
        item.click()
        time.sleep(0.5)

    print("\nSimulação completa com sucesso!")

except Exception as e:
    print("Erro durante a simulação:", str(e))

finally:
    time.sleep(3)
    driver.quit()
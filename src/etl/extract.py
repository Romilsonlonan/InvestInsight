# Importa os módulos necessários do Selenium, pandas, logging e warnings
import logging
import warnings
from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
import pandas as pd 

# Configurações de logging
logger.add("selenium_logs.log", rotation="500 MB", level="DEBUG")  # Define o arquivo de log e o nível de registro

# Configurações de warnings
warnings.simplefilter("default")  # Restaura o comportamento padrão de tratamento de warnings

# Define uma função para configurar e retornar o driver do Chrome
def setup_driver():
    # Instala e configura o driver do Chrome usando o ChromeDriverManager
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Configura o driver
driver = setup_driver()

url = 'https://www.fundamentus.com.br/resultado.php'

# Navega para a URL desejada
driver.get(url)
logger.info(f"Navegando para URL: {url}")

# Localiza a tabela pelo XPath
local_tabela = '/html/body/div[1]/div[2]/table'
elemento = driver.find_element("xpath", local_tabela)
logger.debug(f"Tabela localizada com XPath: {local_tabela}")

# Obtém o HTML da tabela
html_tabela = elemento.get_attribute('outerHTML')
logger.debug("HTML da tabela obtido")

# Lê a tabela usando pandas
tabela = pd.read_html(html_tabela, thousands='.', decimal=',')[0]
logger.info("Tabela lida com sucesso")

# Exibe a tabela
print(tabela)

# Fecha o navegador após a conclusão
driver.quit()
logger.info("Navegador fechado")

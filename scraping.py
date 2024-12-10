import os
import json
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

# Iniciando o driver

driver = webdriver.Chrome()  # Ou o navegador que você estiver usando
driver.get("https://www.bcb.gov.br/controleinflacao/historicotaxasjuros")

# Colhendo informações da tabela
info = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "td"))
        )


datas = []
taxa_selic = []

# preenchendo as listas vazias com base em regras
for contador in range(len(info)):
   if contador >= 1 and (contador - 1) % 8 == 0:
      datas.append(info[contador].text)

   if contador >= 4 and (contador - 4) % 8 == 0:
      taxa_selic.append(info[contador].text)


dict_variacao_selic = {
   'Data': datas,
   'Taxa_Selic': taxa_selic
}

df_selic = pd.DataFrame(dict_variacao_selic)

# Salvando dataframe como CSV
df_selic.to_csv("C:/Projetos Pessoais/DataScience/Taxa_Juros_BC_IA_Previsao/data/dados_scraping",
                sep = ',', index = False, encoding='utf-8')
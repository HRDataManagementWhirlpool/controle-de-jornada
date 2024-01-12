from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import glob
import subprocess
from dotenv import load_dotenv

driver = webdriver.Chrome()
inicio = time.time()
load_dotenv()

class SeleniumController:
    def __init__(self):
        driver.get("https://logincloud.senior.com.br/logon/LogonPoint/tmindex.html")
        
    def iniciar_acesso():
        try:
            element = WebDriverWait(driver, 10).until( #espera até 10s para que o elemento especificado apareça
                EC.presence_of_element_located((By.XPATH, "//input[@id='login']"))
            )
        except Exception as e:
            print(f"Erro ao tentar executar código: {e}")
        else:
            login = driver.find_element(By.XPATH, "//input[@id='login']")
            login.send_keys(os.getenv('LOGIN'))
            
            ### Clicar em Log On
            logOnBtn = driver.find_element(By.ID, "loginBtn")
            logOnBtn.click()
            
            ### Digitar a senha 
            try:
                element = WebDriverWait(driver, 10).until( #espera até 10s para que o elemento especificado apareça
                    EC.presence_of_element_located((By.XPATH, "//input[@id='passwd']"))
                )
            except Exception as e:
                print(f"Erro ao tentar executar código: {e}")
            else:
                passwdSenior = driver.find_element(By.XPATH, "//input[@id='passwd']")
                passwdSenior.send_keys(os.getenv('SENHA')) # Puxa a senha armazenada no .env
                
                ### Clicar em Log On novamente
                logOnBtn = driver.find_element(By.ID, "loginBtn")
                logOnBtn.click()
            ## Função de Login termina aqui
                ### Ao logar Clicar em Acesso e Segurança - Produção
    ## Será uma função para abrir o arquivo de acesso ao RONDA
    def iniciar_sistema(self):
        try:
            element = WebDriverWait(driver, 10).until( #espera até 10s para que o elemento especificado apareça
                EC.presence_of_element_located((By.CLASS_NAME, "storeapp-details-link"))
            )
        except Exception as e:
            print(f"Erro ao tentar executar código: {e}")
        else:
            acesso = driver.find_element(By.CLASS_NAME, "storeapp-details-link")
            acesso.click()
            
            ### Ao clicar, irá baixar um arquivo. Esse arquivo precisa ser clicado para abrir o sistema
            time.sleep(2) # Espera o arquivo ser baixado          
            lista_arquivos= glob.glob("C:/Users/DESOUR10/Downloads/*") #pegando todos os arquivos dentro da pasta downloads
            ultimo_arquivo=max(lista_arquivos, key=os.path.getmtime) #armazenando quem tem a data mais recente dentro da pasta
            driver.quit()
            try:
                # Executa o arquivo usando subprocess
                subprocess.run(ultimo_arquivo, shell=True)
            except Exception as e:
                print(f"Erro ao tentar executar código: {e}")
            ## Termina a função de abertura do RONDA
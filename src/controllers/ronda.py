import pyautogui
import time
import os
from dotenv import load_dotenv

load_dotenv()

class RondaController:
    def __init__(self, dataInicio):
        REs = []
        loop=1
        while loop != 0:
            RE = input('Digite um RE: ')
            REs.append(RE)
            op = input('Deseja inserir outro RE? 1 - Sim    2 - Não\n')
            if op == 2:
                loop = 0

        time.sleep(60)
        pyautogui.PAUSE = 1
        pyautogui.click(640, 409) # Clicar na a área de login 
        pyautogui.write(os.getenv('USER'))
        pyautogui.click(640, 433) # Clicar na a área de senha 
        pyautogui.write(os.getenv('PSSWRD'))
        pyautogui.click(896, 336) # Clicar no Ok
        time.sleep(20) # Esperar para logar no sistema
        for count, RE in enumerate(REs):
            pyautogui.doubleClick(100, 100) # Clicar em Consultar Acessos
            time.sleep(5) # Esperar o carregamento da consulta
            pyautogui.click(405, 90) ## Clicar em Período (405, 90)
            pyautogui.write(dataInicio) # Digitar a data de início 01022023
            pyautogui.doubleClick(405, 115) ## Clicar em Local Físico (405, 115)
            pyautogui.write('1') # Digitar 1 para Brazil
            pyautogui.doubleClick(1310, 90) ## Clicar em Seleção (1310, 90)
            time.sleep(5) # Esperar o carregamento da consulta
            pyautogui.doubleClick(341, 46) # Em empresa inserir o código 100 (231, 46)
            pyautogui.write('100')
            pyautogui.doubleClick(232, 95) # Em Colaborador inserir o RE (232, 95)
            pyautogui.write(RE)
            pyautogui.doubleClick(1155, 50) # Clicar em Ok (1155, 50)
            time.sleep(2) # Esperar o carregamento da consulta
            pyautogui.doubleClick(1310, 120) ## Clicar em Mostrar (1310, 120)
            time.sleep(3)
            ## Salvando Dados
            print(count, RE)
            pyautogui.doubleClick(652, 272) # Baixar .xlsxW
            pyautogui.rightClick() #botão direito na planilha
            pyautogui.click(736, 309) #clica em exportar planilha
            pyautogui.doubleClick(913, 368) #fecha a mensagem de erro
            pyautogui.doubleClick(610, 385) #Seleciona o nome do arquivo
            pyautogui.write(RE) # Escreve o nome do arquivo
            if count == 0:
                pyautogui.doubleClick(610, 385) #Seleciona o nome do arquivo
                pyautogui.write(RE) # Escreve o nome do arquivo
                pyautogui.doubleClick(600, 310) # Clica em Meu Computador
                pyautogui.press('l') #Procura a o Disco Local
                pyautogui.doubleClick(580, 250) 
                pyautogui.press('u') #Procura a pasta Users
                pyautogui.doubleClick(530, 315) #Clica na pasta
                pyautogui.press('d') #Procura o usuário
                pyautogui.doubleClick(540, 280) #Clica na pasta do usuário
                time.sleep(2)
                pyautogui.press('d') #Procura a pasta documentos
                pyautogui.doubleClick(550, 280) #Clica na pasta Documentos
            ## Caso não seja só salvar e confirmar
            pyautogui.doubleClick(840, 385) # Clica em salvar
            pyautogui.doubleClick(685, 420) # Clica em ok
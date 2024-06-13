import json
import os
import re
import time
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from requests import Session
from datetime import date

def tempo():
    time.sleep(16)

def run(playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False) # SE POR = True ele vai ocultar o navegador
    context = browser.new_context(locale='pt-BR')  
    page = context.new_page()
    
    try:
        if os.path.exists('credenciais.json'):
            with open('credenciais.json', 'r') as f:
                credenciais = json.load(f)
        else:
            email = input("\nDigite seu email: ")
            senha = input("Digite sua senha: ")
            credenciais = {'email': email, 'password': senha}
            with open('credenciais.json', 'w') as f:
                json.dump(credenciais, f)

        page.goto("https://blaze1.space/pt/games/category/live-casino?modal=auth&tab=login")  
        page.wait_for_selector('input[name="username"]')
        page.fill('input[name="username"]', credenciais['email'])
        page.wait_for_selector('input[name="password"]')
        page.fill('input[name="password"]', credenciais['password'])
        page.press('input[name="password"]', 'Enter')
        time.sleep(2)
        page.goto("https://blaze1.space/pt/games/baccarat-lobby") 
        iframe_element = page.query_selector('iframe')  
        iframe = iframe_element.content_frame()

        resultados_antigos = [[] for _ in range(6)]
        resultados_antigos1 = [[] for _ in range(6)]
        resultados_antigos3 = [[] for _ in range(6)]
        resultados_antigos5 = [[] for _ in range(6)]
        resultados_antigos6 = [[] for _ in range(6)]
        resultados_antigos7 = [[] for _ in range(6)]
        resultados_antigos8 = [[] for _ in range(6)]
        resultados_antigos9 = [[] for _ in range(6)]
        
        lista_baccarat1 = []
        lista_baccarat2 = []
        lista_baccarat3 = []
        lista_baccarat5 = []
        lista_baccarat6 = []
        lista_baccarat7 = []
        lista_baccarat8 = []
        lista_baccarat9 = []
        
        
        while True:
            try:
                iframe.wait_for_selector('.v_x', timeout=50000)
                html_content = iframe.content()
                soup = BeautifulSoup(html_content, 'html.parser')
                listas_baccarat = [lista_baccarat1, lista_baccarat2, lista_baccarat3, lista_baccarat5, lista_baccarat6, lista_baccarat7, lista_baccarat8, lista_baccarat9]

                for lista in listas_baccarat:
                    if len(lista) > 1:
                        lista.clear()

                #<circle cx="8" cy="8" r="7.2" stroke="#3E8AEE" stroke-width="1.6" fill="" style="max-height: 100%; max-width: 100%;"></circle> <circle cx="3.2" cy="3.2" r="2.8" fill="#F33D3D" stroke="var(--baccaratBgColor)" stroke-width="0.8"></circle>
                
                # BACCARAT 1
                win_containers = soup.find_all('div', id='h22z8qhp17sa0vkh-401')
                for idx, win_container in enumerate(win_containers): #hG_hH pe_pg
                    tables = win_container.find_all('table') # as vezes as class 'ne_nf' e 'nb_nf' podem mudar de acordo com a linguagem do site
                    
                    for table in tables:
                        rows = table.find_all('tr')
                        resultados = [str(row) for row in rows]
                        novos_resultados = [resultado for resultado in resultados if resultado not in resultados_antigos[idx]]
                        if novos_resultados:
                            resultados_antigos[idx] = resultados
                            
                            for novo_resultado in novos_resultados:
                                ultimo_svg = re.findall(r'<svg.*?</svg>', novo_resultado, re.DOTALL)[-1]
                               
                                if 'stroke="#F33D3D"' in ultimo_svg and 'fill="#28BE67"' in ultimo_svg:
                                    print("BACCARAT 1 = EMAPTE VERMELHO")
                                    result1 = 'EV'
                                    lista_baccarat1.append(result1)
                                    
                                    print(lista_baccarat1)
                                
                                elif 'stroke="#3E8AEE"' in ultimo_svg and 'fill="#28BE67"' in ultimo_svg:
                                    print("BACCARAT 1 = EMAPTE AZUL")
                                    result1 = 'EA'
                                    lista_baccarat1.append(result1)
                                 
                                    print(lista_baccarat1)
                                    
                                elif 'stroke="#F33D3D"' in  ultimo_svg:
                                    print("BACCARAT 1 = VERMELHO")
                                    result1 = 'V'
                                    lista_baccarat1.append(result1)
                                 
                                    print(lista_baccarat1)
                                    
                                elif 'stroke="#3E8AEE"' in  ultimo_svg:
                                    print("BACCARAT 1 = AZUL")  
                                    result1 = 'A'
                                    lista_baccarat1.append(result1)
                                   
                                    print(lista_baccarat1)
                                                       
                        else:
                            continue
                
                # BACCARAT 2
                win_containers2 = soup.find_all('div', id='9j3eagurfwmml7z2-404')
                for idx, win_container in enumerate(win_containers2):
                    tables = win_container.find_all('table', class_='ne_nf')
                    for table in tables:
                        rows = table.find_all('tr', class_='ne_nh')
                        resultados = [str(row) for row in rows]
                        novos_resultados1 = [resultado for resultado in resultados if resultado not in resultados_antigos1[idx]]
                        if novos_resultados1:
                            resultados_antigos1[idx] = resultados
                            
                            for novo_resultado in novos_resultados1:
                                ultimo_svg = re.findall(r'<svg.*?</svg>', novo_resultado, re.DOTALL)[-1]
                                
                                if 'stroke="#F33D3D"' in ultimo_svg and 'fill="#28BE67"' in ultimo_svg:
                                    print("BACCARAT 2 = EMAPTE VERMELHO")
                                    result2 = 'EV'
                                    lista_baccarat2.append(result2)
                                   
                                elif 'stroke="#3E8AEE"' in ultimo_svg and 'fill="#28BE67"' in ultimo_svg:
                                    print("BACCARAT 2 = EMAPTE AZUL")
                                    result2 = 'EA'
                                    lista_baccarat2.append(result2)
                                    
                                elif 'stroke="#F33D3D"' in  ultimo_svg:
                                    print("BACCARAT 2 = VERMELHO")
                                    result2 = 'V'
                                    lista_baccarat2.append(result2)
                                  
                                    
                                elif 'stroke="#3E8AEE"' in  ultimo_svg:
                                    print("BACCARAT 1 = AZUL")  
                                    result2 = 'A'
                                    lista_baccarat2.append(result2)
                                                     
                        else:
                            continue
                
                # BACCARAT 3
                win_containers3 = soup.find_all('div', id='cbcf6qas8fscb222-422')
                for idx, win_container in enumerate(win_containers3):
                    tables = win_container.find_all('table', class_='ne_nf')
                    for table in tables:
                        rows = table.find_all('tr', class_='ne_nh')
                        resultados = [str(row) for row in rows]
                        novos_resultados3 = [resultado for resultado in resultados if resultado not in resultados_antigos3[idx]]
                        if novos_resultados3:
                            resultados_antigos3[idx] = resultados
                          
                            for novo_resultado in novos_resultados3:
                                ultimo_svg = re.findall(r'<svg.*?</svg>', novo_resultado, re.DOTALL)[-1]
                                
                                if 'stroke="#F33D3D"' in ultimo_svg and 'fill="#28BE67"' in ultimo_svg:
                                    print("BACCARAT 3 = EMAPTE VERMELHO")
                                    result3 = 'EV'
                                    lista_baccarat3.append(result3)
                                
                                elif 'stroke="#3E8AEE"' in ultimo_svg and 'fill="#28BE67"' in ultimo_svg:
                                    print("BACCARAT 3 = EMAPTE AZUL")
                                    result3 = 'EA'
                                    lista_baccarat3.append(result3)
                                  
                                elif 'stroke="#F33D3D"' in  ultimo_svg:
                                    print("BACCARAT 3 = VERMELHO")
                                    result3 = 'V'
                                    lista_baccarat3.append(result3)
                                  
                                elif 'stroke="#3E8AEE"' in  ultimo_svg:
                                    print("BACCARAT 3 = AZUL")  
                                    result3 = 'A'
                                    lista_baccarat3.append(result3)
                                                     
                        else:
                            continue
                
                # BACCARAT 5
                win_containers5 = soup.find_all('div', id='ne074fgn4bd1150i-411')
                for idx, win_container in enumerate(win_containers5):
                    tables = win_container.find_all('table', class_='ne_nf')
                    for table in tables:
                        rows = table.find_all('tr', class_='ne_nh')
                        resultados = [str(row) for row in rows]
                        novos_resultados5 = [resultado for resultado in resultados if resultado not in resultados_antigos5[idx]]
                        if novos_resultados5:
                            resultados_antigos5[idx] = resultados
                           
                            for novo_resultado in novos_resultados5:
                                ultimo_svg = re.findall(r'<svg.*?</svg>', novo_resultado, re.DOTALL)[-1]
                                
                                if 'stroke="#F33D3D"' in ultimo_svg and 'fill="#28BE67"' in ultimo_svg:
                                    print("BACCARAT 5 = EMAPTE VERMELHO")
                                    result5 = 'EV'
                                    lista_baccarat5.append(result5)
                                 
                                elif 'stroke="#3E8AEE"' in ultimo_svg and 'fill="#28BE67"' in ultimo_svg:
                                    print("BACCARAT 5 = EMAPTE AZUL")
                                    result5 = 'EA'
                                    lista_baccarat5.append(result5)
                                  
                                elif 'stroke="#F33D3D"' in  ultimo_svg:
                                    print("BACCARAT 5 = VERMELHO")
                                    result5 = 'V'
                                    lista_baccarat5.append(result5)
                                  
                                elif 'stroke="#3E8AEE"' in  ultimo_svg:
                                    print("BACCARAT 5 = AZUL")  
                                    result5 = 'A'
                                    lista_baccarat5.append(result5)
                                                      
                        else:
                            continue
                
                # BACCARAT 6
                win_containers6 = soup.find_all('div', id='oq808ojps709qqaf-413')
                for idx, win_container in enumerate(win_containers6):
                    tables = win_container.find_all('table', class_='ne_nf')
                    for table in tables:
                        rows = table.find_all('tr', class_='ne_nh')
                        resultados = [str(row) for row in rows]
                        novos_resultados6 = [resultado for resultado in resultados if resultado not in resultados_antigos6[idx]]
                        if novos_resultados6:
                            resultados_antigos6[idx] = resultados
                            
                            for novo_resultado in novos_resultados6:
                                ultimo_svg = re.findall(r'<svg.*?</svg>', novo_resultado, re.DOTALL)[-1]
                                
                                if 'stroke="#F33D3D"' in ultimo_svg and 'fill="#28BE67"' in ultimo_svg:
                                    print("BACCARAT 6 = EMAPTE VERMELHO")
                                    result6 = 'EV'
                                    lista_baccarat6.append(result6)
                                    
                                elif 'stroke="#3E8AEE"' in ultimo_svg and 'fill="#28BE67"' in ultimo_svg:
                                    print("BACCARAT 6 = EMAPTE AZUL")
                                    result6 = 'EA'
                                    lista_baccarat6.append(result6)
                                
                                elif 'stroke="#F33D3D"' in  ultimo_svg:
                                    print("BACCARAT 6 = VERMELHO")
                                    result6 = 'V'
                                    lista_baccarat6.append(result6)
                                    
                                elif 'stroke="#3E8AEE"' in  ultimo_svg:
                                    print("BACCARAT 6 = AZUL")  
                                    result6 = 'A'
                                    lista_baccarat6.append(result6)
                                                      
                        else:
                            continue
                
                # BACCARAT 7
                win_containers7 = soup.find_all('div', id='bcpirpmfpeobc191-425')
                for idx, win_container in enumerate(win_containers7):
                    tables = win_container.find_all('table', class_='ne_nf')
                    for table in tables:
                        rows = table.find_all('tr', class_='ne_nh')
                        resultados = [str(row) for row in rows]
                        novos_resultados7 = [resultado for resultado in resultados if resultado not in resultados_antigos7[idx]]
                        if novos_resultados7:
                            resultados_antigos7[idx] = resultados
                          
                            for novo_resultado in novos_resultados7:
                                ultimo_svg = re.findall(r'<svg.*?</svg>', novo_resultado, re.DOTALL)[-1]
                                
                                if 'stroke="#F33D3D"' in ultimo_svg and 'fill="#28BE67"' in ultimo_svg:
                                    print("BACCARAT 7 = EMAPTE VERMELHO")
                                    result7 = 'EV'
                                    lista_baccarat7.append(result7)
                                   
                                elif 'stroke="#3E8AEE"' in ultimo_svg and 'fill="#28BE67"' in ultimo_svg:
                                    print("BACCARAT 7 = EMAPTE AZUL")
                                    result7 = 'EA'
                                    lista_baccarat7.append(result7)
                                   
                                elif 'stroke="#F33D3D"' in  ultimo_svg:
                                    print("BACCARAT 7 = VERMELHO")
                                    result7 = 'V'
                                    lista_baccarat7.append(result7)
                                 
                                elif 'stroke="#3E8AEE"' in  ultimo_svg:
                                    print("BACCARAT 7 = AZUL")  
                                    result7 = 'A'
                                    lista_baccarat7.append(result7)
                                                     
                        else:
                            continue
                
                # BACCARAT 8
                win_containers8 = soup.find_all('div', id='bcpirpmfpeobc192-426')
                for idx, win_container in enumerate(win_containers8):
                    tables = win_container.find_all('table', class_='ne_nf')
                    for table in tables:
                        rows = table.find_all('tr', class_='ne_nh')
                        resultados = [str(row) for row in rows]
                        novos_resultados8 = [resultado for resultado in resultados if resultado not in resultados_antigos8[idx]]
                        if novos_resultados8:
                            resultados_antigos8[idx] = resultados
                           
                            for novo_resultado in novos_resultados8:
                                ultimo_svg = re.findall(r'<svg.*?</svg>', novo_resultado, re.DOTALL)[-1]
                                
                                if 'stroke="#F33D3D"' in ultimo_svg and 'fill="#28BE67"' in ultimo_svg:
                                    print("BACCARAT 8 = EMAPTE VERMELHO")
                                    result8 = 'EV'
                                    lista_baccarat8.append(result8)
                                    
                                elif 'stroke="#3E8AEE"' in ultimo_svg and 'fill="#28BE67"' in ultimo_svg:
                                    print("BACCARAT 8 = EMAPTE AZUL")
                                    result8 = 'EA'
                                    lista_baccarat8.append(result8)
                                    
                                elif 'stroke="#F33D3D"' in  ultimo_svg:
                                    print("BACCARAT 8 = VERMELHO")
                                    result8 = 'V'
                                    lista_baccarat8.append(result8)
                                    
                                elif 'stroke="#3E8AEE"' in  ultimo_svg:
                                    print("BACCARAT 8 = AZUL")  
                                    result8 = 'A'
                                    lista_baccarat8.append(result8)
                                                      
                        else:
                            continue
                
                # BACCARAT 9
                win_containers9 = soup.find_all('div', id='bcpirpmfpobc1912-436')
                for idx, win_container in enumerate(win_containers9):
                    tables = win_container.find_all('table', class_='ne_nf')
                    for table in tables:
                        rows = table.find_all('tr', class_='ne_nh')
                        resultados = [str(row) for row in rows]
                        novos_resultados9 = [resultado for resultado in resultados if resultado not in resultados_antigos9[idx]]
                        if novos_resultados9:
                            resultados_antigos9[idx] = resultados
                           
                            for novo_resultado in novos_resultados8:
                                ultimo_svg = re.findall(r'<svg.*?</svg>', novo_resultado, re.DOTALL)[-1]
                                
                                if 'stroke="#F33D3D"' in ultimo_svg and 'fill="#28BE67"' in ultimo_svg:
                                    print("BACCARAT 9 = EMAPTE VERMELHO")
                                    result9 = 'EV'
                                    lista_baccarat9.append(result9)
                                    
                                elif 'stroke="#3E8AEE"' in ultimo_svg and 'fill="#28BE67"' in ultimo_svg:
                                    print("BACCARAT 9 = EMAPTE AZUL")
                                    result9 = 'EA'
                                    lista_baccarat9.append(result9)
                                    
                                elif 'stroke="#F33D3D"' in  ultimo_svg:
                                    print("BACCARAT 9 = VERMELHO")
                                    result9 = 'V'
                                    lista_baccarat9.append(result9)
                                    
                                elif 'stroke="#3E8AEE"' in  ultimo_svg:
                                    print("BACCARAT 9 = AZUL")  
                                    result9 = 'A'
                                    lista_baccarat9.append(result9)
                                                       
                        else:
                            continue
                
                time.sleep(1)

            except Exception as e:
                continue

    except KeyboardInterrupt:
        print("PAROU.")

    finally:
        browser.close()

def main():
    with sync_playwright() as playwright:
        run(playwright)
main()

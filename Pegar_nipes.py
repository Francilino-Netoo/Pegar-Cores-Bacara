import json
import os
import re
import time
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

def tempo():
    time.sleep(16)

def run(playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)  # SE POR = True ele vai ocultar o navegador
    context = browser.new_context(locale='en-US')
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

        page.goto("https://blaze.com/pt/games/category/live-casino?modal=auth&tab=login")
        page.wait_for_selector('input[name="username"]')
        page.fill('input[name="username"]', credenciais['email'])
        page.wait_for_selector('input[name="password"]')
        page.fill('input[name="password"]', credenciais['password'])
        page.press('input[name="password"]', 'Enter')
        time.sleep(2)
        page.goto("https://blaze.com/pt/games/lobby")
        page.goto("https://a8r.evo-games.com/frontend/evo/r2/#category=game_shows")
        page.goto("https://a8r.evo-games.com/frontend/evo/r2/#category=game_shows&game=topcard&table_id=TopCard000000001&vt_id=qfgzfeiyhvch5f34&lobby_launch_id=0fa26bc09e214b47a5278e09c06fe592")
        iframe_element = page.query_selector('iframe')
        iframe = iframe_element.content_frame()
        print(iframe)

        previous_x = None
        
        

        found_initial_x = False  # Flag para indicar se encontramos um resultado com o x inicial

        
        
        while True:
            try:
                iframe.wait_for_selector('.box--ce3ac', timeout=50000)
                time.sleep(2)  # Tempo adicional para garantir a estabilidade da página após carregar

                html_content = iframe.content()
                soup = BeautifulSoup(html_content, 'html.parser')

                win_containers = soup.find_all('div', class_='card--61f40 isTabletDesktop--f9c5b isDesktop--e521d')

                Nipes_casa = []
                Resultado_casa = []
                
                Nipes_visitante = []
                Resultado_visitante = []
                
                for win_container in win_containers:
                    tables = win_container.find_all('span')
                    print(tables,'\n')
                    for table in tables:
                        svgs = table.find_all('svg')
                        for svg in svgs:
                            uses = svg.find_all('use')
                            for use in uses:
                                href = use.get('xlink:href')
                                x_value = use.get('x')
                                
                                if href and x_value:
                                    if not found_initial_x:
                                        # Captura o primeiro resultado com x inicial
                                        #print(x_value)
                                        rank_match = re.search(r'rank-(\w+)', href)
                                        suit_match = re.search(r'suit-(\w+)', href)
                                        if rank_match:
                                            Resultado_casa.append(rank_match.group(1))
                                        if suit_match:
                                            Nipes_casa.append(suit_match.group(1))
                                        previous_x = x_value
                                        found_initial_x = True
                                     
                                    elif x_value != previous_x:
                                        #print(x_value)
                                        # Captura resultados apenas se o x for diferente do inicial
                                        rank_match = re.search(r'rank-(\w+)', href)
                                        suit_match = re.search(r'suit-(\w+)', href)
                                        if rank_match:
                                            Resultado_visitante.append(rank_match.group(1))
                                        if suit_match:
                                            Nipes_visitante.append(suit_match.group(1))
                                        previous_x = x_value  # Atualiza o valor de previous_x
                    
                '''
                if Nipes_casa and found_initial_x:
                    print(f'Nipes_casa: {Nipes_casa[-1]}')

                if Resultado_casa and found_initial_x:
                    print(f'Resultado_casa: {Resultado_casa[-1]}\n')

                if Nipes_visitante and found_initial_x:
                    print(f'Nipes_visitante: {Nipes_visitante[-1]}')

                if Resultado_visitante and found_initial_x:
                    print(f'Resultado_visitante: {Resultado_visitante[-1]}\n')
                '''
                

                time.sleep(1)

            except Exception as e:
                print(f'Error: {e}')
                continue

    except KeyboardInterrupt:
        print("PAROU.")

    finally:
        browser.close()

def main():
    with sync_playwright() as playwright:
        run(playwright)

main()

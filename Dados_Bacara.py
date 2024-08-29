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
    browser = chromium.launch(headless=False)  # Defina headless=True para ocultar o navegador
    context = browser.new_context(locale='pt-BR')  # Configura o contexto com localização em português
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

        # Preenche os campos de login
        page.goto("https://jonbet.com/pt/games/category/live-casino?modal=auth&tab=login")  
        page.wait_for_selector('input[name="username"]')
        page.fill('input[name="username"]', credenciais['email'])
        page.wait_for_selector('input[name="password"]')
        page.fill('input[name="password"]', credenciais['password'])
        page.press('input[name="password"]', 'Enter')
        time.sleep(2)

        # Navega para a página que contém o iframe desejado
        page.goto("https://jonbet.com/pt/games/evolution-gaming-lobby-3") 
        
        # Captura todos os iframes na página
        iframes = page.query_selector_all('iframe')
        
        # Verifica se existe o segundo iframe (índice 1, pois índice 0 é o primeiro)
        if len(iframes) > 2:
            iframe_element = iframes[1]  
            iframe = iframe_element.content_frame()
            print(iframe.url)  # Exibe a URL do conteúdo do segundo iframe

            # Aqui você pode continuar seu processamento dentro do iframe
            # Por exemplo, esperar por um seletor dentro do iframe
            iframe.wait_for_selector('.customScroll--0a6dc', timeout=50000)
            html_content = iframe.content()
            soup = BeautifulSoup(html_content, 'html.parser')
            print(soup)

            time.sleep(500000)
        resultados_antigos = [[] for _ in range(6)]
        lista_baccarat1 = []
        
        while True:
            try:
                # Seu código de processamento dentro do iframe continua aqui

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

if __name__ == "__main__":
    main()
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import threading
import time

#armazenar resultado
urls_visitados = set()
resultados = {}
lock = threading.Lock()

def buscar_palavra_na_pagina(url, palavra):
    
    try:
        print(f"Buscando em: {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # analisa o html
        soup = BeautifulSoup(response.text, 'html.parser')

        conteudo = soup.get_text().lower()
        palavra_encontrada = palavra.lower() in conteudo

        with lock:
            resultados[url] = palavra_encontrada

        # pegar todos os links da pagina
        links = soup.find_all('a', href=True)
        for link in links:
            url_completa = urljoin(url, link['href'])

            # Garante que só navegamos dentro do mesmo domínio
            if url_completa.startswith(url) and url_completa not in urls_visitados:
                with lock:
                    urls_visitados.add(url_completa)
                # Cria uma nova thread para processar o link
                thread = threading.Thread(target=buscar_palavra_na_pagina, args=(url_completa, palavra))
                thread.start()
                thread.join()  # Aguarda a conclusão da thread

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")

def buscar_palavra_no_site(url_inicial, palavra, profundidade_maxima=3):
    """
    Inicia a busca paralelizada de uma palavra em um site.

    Parâmetros:
        url_inicial (str): A URL inicial do site.
        palavra (str): A palavra a ser buscada.
        profundidade_maxima (int): A profundidade máxima de navegação (padrão: 3).
    """
    global urls_visitados, resultados

    # Inicia a busca na URL inicial
    urls_visitados.add(url_inicial)
    thread_inicial = threading.Thread(target=buscar_palavra_na_pagina, args=(url_inicial, palavra))
    thread_inicial.start()
    thread_inicial.join()  # Aguarda a conclusão da thread inicial

if __name__ == "__main__":
    url_inicial = input("Digite a URL inicial do site (ex.: https://www.exemplo.com): ")
    palavra = input("Digite a palavra a ser buscada: ")

    # Medir tempo de execução
    inicio = time.time()
    buscar_palavra_no_site(url_inicial, palavra)
    fim = time.time()

    print("\nResultados da busca:")
    for url, encontrada in resultados.items():
        status = "Encontrada" if encontrada else "Não encontrada"
        print(f"{url}: Palavra '{palavra}' {status}")

    print(f"\nTempo de execução: {fim - inicio:.2f} segundos")
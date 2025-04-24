import requests

BASE_URL = 'http://127.0.0.1:5000'

def listar_produtos():
    try:
        response = requests.get(f'{BASE_URL}/produtos')
        if response.status_code == 200:
            produtos = response.json()
            if not produtos:
                print("Nenhum produto cadastrado.")
            else:
                print("\nLista de Produtos:")
                for produto in produtos:
                    # Converte o preço para float antes de formatar
                    preco = float(produto['preco'])
                    print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preço: R${preco:.2f}")
        else:
            print(f"Erro ao listar produtos. Código de status: {response.status_code}")
    except Exception as e:
        print(f"Erro: {e}")
        
def adicionar_produto(nome, preco):
    try:
        novo_produto = {'nome': nome, 'preco': preco}
        response = requests.post(f'{BASE_URL}/produtos', json=novo_produto)
        response.raise_for_status()  # Levanta exceção para códigos 4xx/5xx
        print("Produto adicionado com sucesso!")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao adicionar produto: {e}")
        
def buscar_produto(id):
    try:
        response = requests.get(f'{BASE_URL}/produtos/{id}')
        if response.status_code == 200:
            produto = response.json()
            print("\nProduto Encontrado:")
            print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preço: R${float(produto['preco']):.2f}")
        elif response.status_code == 404:
            print("Produto não encontrado.")
        else:
            print(f"Erro ao buscar produto. Código: {response.status_code}")
    except Exception as e:
        print(f"Erro na requisição: {e}")

def menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Listar Produtos")
        print("2 - Adicionar Produto")
        print("3 - Buscar Produto por ID")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            listar_produtos()
        elif opcao == '2':
            nome = input("Nome do produto: ").strip()
            try:
                preco = float(input("Preço do produto: ").strip())
                if preco <= 0:
                    print("O preço deve ser maior que zero.")
                    continue
                adicionar_produto(nome, preco)
            except ValueError:
                print("Por favor, insira um valor numérico válido para o preço.")
        elif opcao == '3':
            id = input("ID do produto: ").strip()  # Mantém como string
            buscar_produto(id)  # Envia como string
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")
            
if __name__ == '__main__':
    print("=== Cliente de API de Produtos ===")
    menu()
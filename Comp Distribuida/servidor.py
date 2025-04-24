from flask import Flask, request, jsonify
import csv
import os
from typing import List, Dict, Optional

app = Flask(__name__)
DATABASE = 'produtos.csv'

def inicializar_arquivo():
    """Cria o arquivo CSV com cabeçalho se não existir"""
    if not os.path.exists(DATABASE):
        with open(DATABASE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'nome', 'preco'])

def ler_produtos() -> List[Dict[str, str]]:
    """Lê todos os produtos do arquivo CSV"""
    inicializar_arquivo()
    produtos = []
    try:
        with open(DATABASE, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            produtos = list(reader)
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
    return produtos

def salvar_produtos(produtos: List[Dict[str, str]]) -> None:
    """Salva a lista de produtos no arquivo CSV"""
    try:
        with open(DATABASE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'nome', 'preco'])
            writer.writeheader()
            writer.writerows(produtos)
    except Exception as e:
        print(f"Erro ao salvar produtos: {e}")

def proximo_id(produtos: List[Dict[str, str]]) -> str:
    """Gera o próximo ID disponível"""
    if not produtos:
        return '1'
    ids = [int(p['id']) for p in produtos]
    return str(max(ids) + 1)

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    produtos = ler_produtos()
    # Converte os preços para float antes de retornar
    produtos = [{'id': p['id'], 'nome': p['nome'], 'preco': float(p['preco'])} for p in produtos]
    return jsonify(produtos)

@app.route('/produtos', methods=['POST'])
def adicionar_produto():
    """Adiciona um novo produto"""
    novo_produto = request.json
    
    # Validação dos dados
    if not novo_produto or 'nome' not in novo_produto or 'preco' not in novo_produto:
        return jsonify({'erro': 'Nome e preço são obrigatórios'}), 400
    
    try:
        preco = float(novo_produto['preco'])
        if preco <= 0:
            return jsonify({'erro': 'Preço deve ser maior que zero'}), 400
    except ValueError:
        return jsonify({'erro': 'Preço deve ser um número válido'}), 400
    
    nome = novo_produto['nome'].strip()
    if not nome:
        return jsonify({'erro': 'Nome não pode estar vazio'}), 400
    
    produtos = ler_produtos()
    novo_id = proximo_id(produtos)
    
    produto = {
        'id': novo_id,
        'nome': nome,
        'preco': str(round(preco, 2))  # Armazena como string com 2 decimais
    }
    
    produtos.append(produto)
    salvar_produtos(produtos)
    
    return jsonify({
        'mensagem': 'Produto adicionado com sucesso',
        'produto': produto
    }), 201

@app.route('/produtos/<id>', methods=['GET'])
def buscar_produto(id):
    produtos = ler_produtos()
    produto = next((p for p in produtos if p['id'] == str(id)), None)  # Compara como strings
    
    if produto:
        return jsonify(produto)
    return jsonify({'erro': 'Produto não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
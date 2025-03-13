# Servidor (data e hora)

import socket
from datetime import datetime

def iniciar_servidor():
    HOST = '127.0.0.1' # IPV4
    PORT = 65432

    # Criando o socket TCP/IP

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Vinculando o socket ao endereço e porta
        s.bind((HOST, PORT))

        # Escutando por conexões
        s.listen()
        print(f"Servidor iniciado em {HOST}:{PORT}. Aguardando conexões...")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Conectado por {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    
                    if data.decode().strip().lower() == "data e hora":
                        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        resposta = f"Data e hora atual: {agora}"
                        conn.sendall(resposta.encode())
                    else:
                        conn.sendall("Mensagem inválida...")

if __name__ == "__main__":
    iniciar_servidor()
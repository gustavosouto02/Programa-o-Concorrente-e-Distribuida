import socket

def iniciar_servidor():
    HOST = '127.0.0.1'  # IPV4
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

                    if data.decode().strip().lower() == "fatorial":
                        resposta = "numero"
                        conn.sendall(resposta.encode())  # Envia a solicitação de número

                        data = conn.recv(1024)
                        try:
                            n = int(data.decode())  # Converte o número recebido para inteiro
                            print(f"O número recebido é: {n}")

                            # Calcula o fatorial
                            fatorial = 1
                            for i in range(1, n + 1):
                                fatorial *= i

                            resposta = f"O fatorial de {n} é {fatorial}"
                            conn.sendall(resposta.encode())  # Envia o resultado
                            print(f"Fatorial enviado.")
                        except ValueError:
                            conn.sendall("Erro: Número inválido.".encode())
                    else:
                        conn.sendall("Mensagem inválida...".encode())

if __name__ == "__main__":
    iniciar_servidor()
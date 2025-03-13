import socket

def iniciar_cliente():
    HOST = '127.0.0.1'  # IPV4
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Conectado ao servidor: solicitando fatorial...")

        s.sendall(b"fatorial")  # Envia a solicitação de fatorial
        data = s.recv(1024)

        if data.decode() == "numero":
            while True:
                Num = input("Digite um número para calcular o fatorial: ")
                try:
                    # Tenta converter a entrada para inteiro
                    int(Num)
                    break
                except ValueError:
                    print("Erro: Digite um número válido.")

            s.sendall(Num.encode())  # Envia o número como string
            data = s.recv(1024)  # Recebe a resposta do servidor
            print(f"Resposta do servidor: {data.decode()}")
        else:
            print(f"Resposta inesperada do servidor: {data.decode()}")

if __name__ == "__main__":
    iniciar_cliente()
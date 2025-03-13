#Cliente

import socket
def iniciar_cliente():
    HOST = '127.0.0.1' #IPV4
    PORT = 65432
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Conectado ao servidor: solicitando data e hora...")
        
        s.sendall(b"data e hora")
        data = s.recv(1024)
        
        print(f"Resposta ao servidor: {data.decode()}")
        
if __name__ == "__main__":
    iniciar_cliente()
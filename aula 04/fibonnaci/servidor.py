import socket 

def calc_fibonnaci():
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]

def iniciar_servidor():
    
    HOST = '127.0.0.1'  # IPV4
    PORT = 65432
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(HOST, PORT)
        
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
                    
                    if data.decode().strip().lower() == "fibonnaci":
                        resposta = "numero"
                        conn.sendall(resposta.encode())
                        
                        data = conn.recv(1024)
                        
                
        
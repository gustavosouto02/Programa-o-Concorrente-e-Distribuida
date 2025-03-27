import threading
import time

# Cria um semáforo que permite no máximo 3 threads acessarem simultaneamente
S = threading.Semaphore(3)  # Limite de 3 threads concorrentes
X = 1
def AcessoRecurso(thread_id):
    global X 
    """Função que simula o acesso a um recurso limitado"""
    print(f"Thread {thread_id} tentando acessar o recurso...")
    
    # Adquire o semáforo (bloqueia se já houver 3 threads acessando)
    with S:
        # Este bloco só é executado quando o semáforo é adquirido
        print(f"Thread {thread_id} acessou o recurso.")
        
        # Simula o tempo de uso do recurso (1 segundo)
        threading.Event().wait(1)
        X = X * 2    
    # O semáforo é liberado automaticamente ao sair do bloco 'with'
    print(f"Thread {thread_id} liberou o recurso.")

# Cria 5 threads que tentarão acessar o recurso
threads = [threading.Thread(target=AcessoRecurso, args=(i,)) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("Encerrando...")
print(f"Valor final de X: {X}")
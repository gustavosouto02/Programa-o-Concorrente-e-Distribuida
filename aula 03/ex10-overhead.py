import threading
import time

Contador = 0
L = threading.Lock()
TempoTotal = 0.0

def Incrementar():
    global Contador, TempoTotal
    t0 = time.time()
    for _ in range(1000000):
        with L:
            Contador += 1
    tf = time.time()
    delta_t = tf - t0
    with L:
        TempoTotal += delta_t 
    print(f"Tempo gasto: {delta_t:.4f} segundos")

# Criando e iniciando as threads
threads = [threading.Thread(target=Incrementar) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Contador: {Contador} vezes")
print(f"Tempo total gasto: {TempoTotal:.4f} segundos")

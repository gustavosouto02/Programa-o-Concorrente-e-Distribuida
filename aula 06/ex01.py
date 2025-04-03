import time
import threading

def tarefa_io(id_tarefa):
    print(f"Tarefa {id_tarefa} iniciada.")
    time.sleep(2) 
    print(f"Tarefa {id_tarefa} concluida")

def main_sequencial():
    t0 = time.time()
    for i in range(4): tarefa_io(i)
    tf = time.time()
    print(f"Tempo sequencial: {tf - t0:.4f} seg")


def main_paralela():
    t0 = time.time()
    threads = []
    for i in range(4):
        t = threading.Thread(target= tarefa_io, args= (i,))
        threads.append(t)
        t.start()
    for t in threads : t.join()
    tf = time.time()
    print(f"Tempo paralelizado: {tf - t0:.4f} seg")

main_sequencial()    
main_paralela()

# Lei de Amdahl
# T(N) = B * T(1) + (1-B) * (T(1)/N)

# SpeedUp máximo
# S (n) = 1 / B + ((1-B)/N)

# B = sequencial / (1-B) = paralelizada / N = numero de processadores
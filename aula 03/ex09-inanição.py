import threading
import time

AP_contador = 0 #contador de alta prioridade
BP_contador = 0 #contador de baixa prioridade

L = threading.Lock()

def AltaPrioridade():
    global AP_contador
    while True:
        with L :
            print("[AltaPrioridade] usando o recurso")
            AP_contador += 1
            time.sleep(0.5)

def BaixaPrioridade():
    global BP_contador
    while True:
        with L :
            print("[BaixaPrioridade] usando o recurso")
            BP_contador += 1
            time.sleep(0.5)

# criando as threads

t_AP = threading.Thread(target= AltaPrioridade, daemon=True)
t_BP = threading.Thread(target= BaixaPrioridade, daemon=True)

t_AP.start()
t_BP.start()

time.sleep(10)

print("\nRelatório:")
print(f"Thread de alta prioridade: {AP_contador} vezes")
print(f"Thread de baixa prioridade: {BP_contador} vezes")
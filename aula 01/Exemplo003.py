# estado do processo com input
import psutil

def estado_processo(pid):
    try:
        processo = psutil.Process(pid)
        estado = processo.status()
        return estado
    except psutil.NoSuchProcess:
        return "Processo nao encontrado"
    
# Exemplo de uso

pid = int(input("Digite o numero do processo: "))

estado = estado_processo(pid)

print(f"O estado do processo com PID {pid} é {estado}!")
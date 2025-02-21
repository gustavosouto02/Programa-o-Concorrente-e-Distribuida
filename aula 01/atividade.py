'''
# Q 02 MAIOR USO DA CPU
import psutil

def cpu_processo():
    processo = []

    # itera todos os processo e coleta dados da cpu
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            # Ignora o processo (PID 0)
            if proc.info['pid'] != 0:
                processo.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # ordenar processos
    processo.sort(key=lambda p: p['cpu_percent'], reverse=True)

    # processo com maior uso
    if processo:
        top_processo = processo[0]
        print(f"Processo com maior uso de CPU:\nPID: {top_processo['pid']}, Nome: {top_processo['name']}, CPU: {top_processo['cpu_percent']}%")
    else:
        print("Nenhum processo encontrado.")

# chamar a função
print("Iniciando a coleta de processos...")
cpu_processo()
'''

'''
Questao 3
# Monitorar uso de memoria fisica:
import psutil

def obter_memoria(pid):
    try:
        processo = psutil.Process(pid)
        memoria = processo.memory_info()
        memoriaFisica = memoria.rss / (1024 * 1024)  # Converte de bytes para MB

        return memoriaFisica
    except psutil.NoSuchProcess:
        return None 
    
pid = int(input("Digite o PID do processo: ")) 
MF = obter_memoria(pid)

if MF is not None:
    print(f"Processo ID: {pid}")
    print(f"Memória Física: {MF:.3f} MB")
else:
    print(f"O processo com PID {pid} não foi encontrado.")
'''

'''
Questao 4

Somar a memoria fisica de todos processos ativos:

import psutil

def soma_memoria():
    memoriaTotal = 0

    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            # memoria fisica dos processos
            memoriaTotal += proc.info['memory_info'].rss
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    memoriaTotalMB = memoriaTotal / (1024 * 1024)
    return memoriaTotalMB

memoria = soma_memoria()
print(f"A soma das memorias fisicas usadas(rss) de todos os processos é : {memoria:.2f} MB")
'''
'''
# Listar Processos que utilizam mais que 100 MB
import psutil

def listar_processos():
    processos100MB = []

    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            memoriaFisica = proc.info['memory_info'].rss / (1024 * 1024)

            if memoriaFisica > 100:
                processos100MB.append((proc.info['pid'], proc.info['name'], memoriaFisica))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return processos100MB

processos = listar_processos()

if (processos):
    print(f"Processos que estao utilizando mais que 100 MB(rss): \n")
    for pid, nome, memoria in processos:
        print(f"PID: {pid}, Nome: {nome}, Memoria: {memoria:.2f} MB")
    else:
        ("Nenhum processo encontrado.")
'''
'''
#Listar processos em estado 'Sleeping'
import psutil

def listar_processos():
    processos_sleeping = []

    for proc in psutil.process_iter(['pid', 'name', 'status']):
        try:
            if proc.info['status'] == psutil.STATUS_SLEEPING:
                processos_sleeping.append((proc.info['pid'], proc.info['name'], proc.info['status']))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    return processos_sleeping

processos = listar_processos()

if processos:
    print(f"Processos em estado 'sleeping':\n")
    for pid, nome, status in processos:
        print(f"PID: {pid}, Nome: {nome}, Status: {status}")
else:
    print("Nenhum processo em estado 'sleeping' encontrado.")
'''
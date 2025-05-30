'''
# Q 01: Crie um programa que liste todos os processos ativos no sistema, exibindo seus PIDs, nomes e estados (ex.: "running", "sleeping").

import psutil

for proc in psutil.process_iter(['pid', 'name', 'status']):
    try: 
        if proc.info['status'] == psutil.STATUS_RUNNING:
            print(f"PID: {proc.info['pid']}, Nome: {proc.info['name']}, Estado: {proc.info['status']}")
    except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
'''

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
'''
import psutil   

def monitorar_disco(pid):

    try:
        processo = psutil.Process(pid)
        io_info = processo.io_counters()

        print(f"Monitorando o uso de disco do processo {pid} ({processo.name()})...\n")

        print(f"PID: {pid}, Nome: {processo.name()}, ")
        print(f"Leitura de disco: {io_info.read_bytes / (1024 * 1024):.2f} MB")
        print(f"Escrita de disco: {io_info.write_bytes / (1024 * 1024):.2f} MB")

    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass


pid = int(input("Digite o PID do processo: \n"))
monitorar_disco(pid)
'''

'''import psutil

def terminar_processo(pid):
    try:
        processo = psutil.Process(pid)
        print(f"Terminando processo {pid} ({processo.name()})...\n")
        processo.terminate()

        print("Processo terminado com sucesso.\n")
    except (psutil.NoSuchProcess):
        print(f"Processo com numero ")
    except psutil.AccessDenied:
        print("Erro: Acesso negado. Execute o script como administrador.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    
pid = int(input("Digite o PID do processo que deseja encerrar: \n"))
terminar_processo(pid)'''

'''import psutil

def listar_processos_memoria():
    processos = []

    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            memoria_rss = proc.info['memory_info'].rss / (1024 * 1024) 
            processos.append((proc.info['pid'], proc.info['name'], memoria_rss))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Ordenar pelo uso de memória (RSS) em ordem decrescente
    processos.sort(key=lambda p: p[2], reverse=True)

    print(f"{'PID':<10} {'Nome':<30} {'Memória (MB)'}")
    print("=" * 50)
    for pid, nome, memoria in processos:
        print(f"{pid:<10} {nome:<30} {memoria:.2f} MB")

listar_processos_memoria()'''

'''import psutil

def listar_cpu50():
    processos = []

    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            uso_cpu = proc.cpu_percent()
            if uso_cpu > 50:
                processos.append((proc.info['pid'], proc.info['name'], uso_cpu))
        except ( psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    processos.sort(key=lambda p: p[2], reverse=True)

    if processos:
        print(f"{'PID':<10} {"Name":<30} {'Uso de Cpu (%)'}")
        print("=" * 50)
        for pid, nome, cpu in processos:
            print(f"{pid:<10} {nome:<30} {cpu:.2f} %")
    else:
        print("Nenhum processo esta consumindo mais de 50 % da cpu.\n")

listar_cpu50()'''

'''import psutil
import time 

def monitorar_rede(pid, intervalo =2):
    try:
        processo = psutil.Process(pid)
        print(f"Monitorando o uso de rede do processo PID: {pid} ({processo.name()})")
        print("=" * 60)

        while True:
            try:
                net_io = processo.io_counters() #Obtem estatisticas de in/out
                bytes_enviados = net_io.write_bytes
                bytes_recebidos = net_io.read_bytes

                print(f"Bytes enviados: {bytes_enviados / (1024 * 1024)} MB")
                print(f"Bytes recebidos: {bytes_recebidos / (1024 * 1024)} MB")

                sair = input("\nPressione Enter para continuar ou digite 'sair' para parar: ")
                if sair.lower() == "sair":
                    print("\nMonitoramento encerrado pelo usuario.")
                    break

                time.sleep(intervalo)

            except(psutil.NoSuchProcess, psutil.AccessDenied):
                print("Processo nao existe ou acesso nao permitido. \n")        
                break

    except psutil.NoSuchProcess:
        print("Processo com PID: {pid} nao encontrado. \n")   

try:

    pid = int(input("Digite o PID do processo a ser monitorado: "))
    monitorar_rede(pid)

except ValueError:
    print("\n Entrada invalida. Digite um numero inteiro para o PID.")

'''
'''
import psutil

def listar_vms(limite_gb = 1):
    processos = []

    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            vms_gb = proc.info['memory_info'].vms / (1024 ** 3) # Converter para GB

            if vms_gb > limite_gb:
                processos.append((proc.info['pid'], proc.info['name'], vms_gb))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    if processos:
        print(f"\nProcessos usando mais de {limite_gb} GB de memoria virtual: \n")
        for pid, nome, vms in sorted(processos, key=lambda p: p[2], reverse=True):
            print(f"PID: {pid}, Nome: {nome}, Memoria VMS: {vms:.2f} GB")
        
    else:
        print("\nNenhum processo esta usando mais de {limite_gb} GB de VMS")

listar_vms()'''

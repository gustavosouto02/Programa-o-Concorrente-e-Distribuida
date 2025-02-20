import psutil

def cpu_processo(cpu):
    processo = []

    # itera todos os processo e coleta dados da cpu
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
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
    cpu_processo()
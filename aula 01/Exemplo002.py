import psutil

def obter_memoria_processo(pid):
    try:
        processo = psutil.Process(pid)

        memoria = processo.memory_info()
        memoria_fisica = memoria.rss / (1024 * 1024)
        memoria_virtual = memoria.vms / (1024 * 1024)
        
        return memoria_fisica, memoria_virtual
    except psutil.NoSuchProcess:
        return None, None

pid = 0
MF, MV = obter_memoria_processo(pid)
if MF is not None:
    print(f"Processo ID: {pid}")
    print(f"Memoria Fisica: {MF:.3f}")
    print(f"Memoria Virtual: {MV:.3f}")
else:
    print(f"O processo com PID {pid} nao foi encontrado")
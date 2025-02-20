import psutil

for proc in psutil.process_iter(['pid', 'name', 'status']):
    try: 
        if proc.info['status'] == psutil.STATUS_RUNNING:
            print(f"PID: {proc.info['pid']}, Nome: {proc.info['name']}, Estado: {proc.info['status']}")
    except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
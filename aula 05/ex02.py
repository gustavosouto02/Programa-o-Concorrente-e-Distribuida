import threading

B = threading.Barrier(3)

def trabalho(thread_id):
    print(f"Thread {thread_id} iniciada")
    threading.Event().wait(1)
    print(f"Thread {thread_id} chegou à barreira")
    B.wait(1)
    print(f"Thread {thread_id} passsou da barreira")
    
threads = [threading.Thread(target= trabalho, args= (i,)) for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()

print("Fim.")
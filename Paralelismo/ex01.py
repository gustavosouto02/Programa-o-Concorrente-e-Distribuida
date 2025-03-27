import random
import time
import threading

# Função principal do QuickSort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]  # Elementos menores ou iguais ao pivô
    right = [x for x in arr[:-1] if x > pivot]  # Elementos maiores que o pivô
    return quicksort(left) + [pivot] + quicksort(right)

# Função para ordenar uma sublista em uma thread
def quicksort_paralela(arr, result, index):
    result[index] = quicksort(arr)

# Função para gerar números aleatórios
def gerar_numeros_aleatorios(n=100, min_val=1, max_val=200):
    return [random.randint(min_val, max_val) for _ in range(n)]

# Função principal para testar o QuickSort
if __name__ == "__main__":
    # Gerar números aleatórios
    numeros = gerar_numeros_aleatorios(n=100)
    print("Primeiros 10 números antes da ordenação:", numeros[:10])

    # Tempo de execução sequencial
    inicio_seq = time.time()
    numeros_ordenados_seq = quicksort(numeros)
    fim_seq = time.time()

    print("Primeiros 10 números após a ordenação sequencial:", numeros_ordenados_seq[:10])
    print(f"Tempo de execução do sequencial: {fim_seq - inicio_seq:.6f} segundos")

    # Tempo de execução paralelo
    inicio_par = time.time()

    # Dividir a lista em duas partes
    pivot = numeros[-1]
    left = [x for x in numeros[:-1] if x <= pivot]
    right = [x for x in numeros[:-1] if x > pivot]

    # Criar threads para ordenar sublistas
    result = [None, None]  # Armazenar dados
    thread_left = threading.Thread(target=quicksort_paralela, args=(left, result, 0))
    thread_right = threading.Thread(target=quicksort_paralela, args=(right, result, 1))

    # Iniciar as threads
    thread_left.start()
    thread_right.start()

    # Aguardar a conclusão das threads
    thread_left.join()
    thread_right.join()

    # Combinar os resultados
    numeros_ordenados_par = result[0] + [pivot] + result[1]

    fim_par = time.time()

    print("Primeiros 10 números após a ordenação paralelizada:", numeros_ordenados_par[:10])
    print(f"Tempo de execução do QuickSort paralelizado: {fim_par - inicio_par:.6f} segundos")

    # Verificar se a lista está corretamente ordenada
    if numeros_ordenados_par == sorted(numeros):
        print("A lista está corretamente ordenada.")
    else:
        print("Erro: A lista não está corretamente ordenada.")
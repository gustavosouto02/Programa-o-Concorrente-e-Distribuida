'''
Q01 Divida a multiplicação de duas matrizes 4 x 4 entre 4 threads.
Observação:
Suponha que as primeiras linhas do seu script sejam:
import threading
matriz_a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matriz_b = [[16, 15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]]
resultado = [[0]*4 for _ in range(4)]
lock = threading.Lock()


Q02 Determine a lista com todos os números primos entre 1 e 1.000.000 usando 5 threads.
Observação:
Divida o intervalo entre as threads e combine os resultados. Ademais, considere que as primeiras linhas
do seu script sejam:
import threading
import math
primos = []
lock = threading.Lock()


Q03 Escreva script em Python para determinar a média e o desvio padrão de um conjunto de 100.000
números gerados aleatoriamente usando 3 threads. Gere uma planilha do Excel para confirmar o
resultado que você obteve.


Q04 Escreva um script em Python para resolver um sistema de 𝒏 equações lineares e 𝒏 incógnitas usando o
Método de Cramer, distribuindo o processamento em 𝒏 threads.
Observação:
Dado um sistema linear na forma matricial 𝐴𝑋 = 𝐵 onde 𝐴 é a matriz dos coeficientes (𝑛 × 𝑛), 𝑋 é o
vetor das incógnitas (𝑛 × 1), 𝐵 é o vetor dos termos independentes (𝑛 × 1). O método de Cramer
calcula cada incógnita 𝑥𝑖 como
𝑥𝑖 = det(𝐴𝑖)
det(𝐴)
Onde det(A) é o determinante de A, e 𝐴𝑖 é a matriz obtida substituindo a coluna i de A pelo vetor B.
'''
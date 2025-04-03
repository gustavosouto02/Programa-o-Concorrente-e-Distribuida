import matplotlib.pyplot as plt


# Função para calcular speedup
def speedup(f, p_values):
    results = [(p, 1/((1-f) + f/p)) for p in p_values]
    return results

f = 0.6 # 60% paralelizável
p_values = [1, 2, 3, 4, 8, 16, 32]
s_values = speedup(f, p_values)

for p, sp in s_values:
    print(f"{p}\t{sp}")
    
plt.plot(p_values, [s[1] for s in s_values], marker = 'o')
plt.xlabel("Número de processadores (p)")
plt.ylabel("SpeedUp (S(p))")
plt.title("S(p) versus p para {f}")
plt.grid
plt.show()
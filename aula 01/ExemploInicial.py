n = 48
numDivisores = 0

for i in range (1, n + 1):  
    if n % i == 0:
        numDivisores = numDivisores + 1
        print(i)


print("numero de divisores:")
print(numDivisores)
import time 

def eratostenes(n):
    primos = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if (primos[p] == True):
            for i in range(p * p, n + 1, p):
                primos[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primos[p]]

inicio = time.time()
res = eratostenes(100000)
fin = time.time()

print(res)
print ("Tiempo de ejecución: ", fin - inicio)   

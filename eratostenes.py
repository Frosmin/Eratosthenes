# import time 

# def eratostenes(n):
#     primos = [True] * (n + 1)
#     p = 2
#     while (p * p <= n):
#         if (primos[p] == True):
#             for i in range(p * p, n + 1, p):
#                 primos[i] = False
#         p += 1
#     return [p for p in range(2, n + 1) if primos[p]]

# inicio = time.time()
# res = eratostenes(100000)
# fin = time.time()

# print(res)
# print ("Tiempo de ejecución: ", fin - inicio)   


import matplotlib.pyplot as plt

# Datos de los tiempos de ejecución para Java y JavaScript
n_values = [10000, 100000, 1000000, 10000000, 100000000]
java_times = [0.05, 0.4, 4.0, 35.0, 350.0]
js_times = [0.07, 0.6, 6.0, 60.0, 600.0]

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(n_values, java_times, label='Java', marker='o', color='b')
plt.plot(n_values, js_times, label='JavaScript', marker='o', color='r')

# Agregar etiquetas y título
plt.xlabel('Valor de n')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Comparación de tiempos de ejecución entre Java y JavaScript para la Criba de Eratóstenes')
plt.xscale('log')  # Escala logarítmica para el eje x
plt.yscale('log')  # Escala logarítmica para el eje y
plt.legend()

# Mostrar la gráfica
plt.grid(True, which="both", ls="--")
plt.show()


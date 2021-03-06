import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

# Se defube un array x para el manejo del factor de calidad en un restaurante
x = np.arange(0, 11, 1)

bajo = sk.trimf(x, [0, 0, 5])
medio = sk.trimf(x, [0, 5, 10])

# Grafica

plt.figure()
plt.plot(x, bajo, 'b', linewidth=1.5, label='Bajo')
plt.plot(x, medio, 'b', linewidth=1.5, label='Medio')

plt.title('Funcion union Maxima')
plt.ylabel('Membresia')
plt.xlabel('Velocidad km/h')
plt.legend(loc='center right', bbox_to_anchor=(
    1.25, 0.5), ncol=1, fancybox=True, shadow=True)

plt.axvline(x)

i = 0
while i <= range(10):
    plt.axvline(i, ymin=0, ymax=10, color='g', licestyle='-.')

plt.plot(0, 1, marker='o', markersize=10, color='g')
plt.plot(1, 0.8, marker='o', markersize=10, color='g')
plt.plot(2, 0.6, marker='o', markersize=10, color='g')
plt.plot(3, 0.6, marker='o', markersize=10, color='g')
plt.plot(4, 0.8, marker='o', markersize=10, color='g')
plt.plot(5, 1, marker='o', markersize=10, color='g')

plt.plot(6, 0.8, marker='o', markersize=10, color='g')
plt.plot(7, 0.6, marker='o', markersize=10, color='g')
plt.plot(8, 0.4, marker='o', markersize=10, color='g')
plt.plot(9, 0.2, marker='o', markersize=10, color='g')
plt.plot(10, 0, marker='o', markersize=10, color='g')

plt.show()

sk.fuzzy_and(x, bajo, x, medio)

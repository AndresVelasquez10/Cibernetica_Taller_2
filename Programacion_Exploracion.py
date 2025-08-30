import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, X0, N):
    X = np.zeros(N)
    X[0] = X0
    for n in range(N-1):
        X[n+1] = r * X[n] * (1 - X[n])
    return X

# Parámetros
X0 = 0.5   # condición inicial
N = 200    # número de iteraciones
r = 2.5    # valor de r (puedes cambiarlo

#grafica
X = logistic_map(r, X0, N)

plt.plot(range(N), X, marker='o', markersize=3, linestyle='-')
plt.title(f"Mapa logístico con r={r}")
plt.xlabel("Iteración (n)")
plt.ylabel("X")
plt.grid(True)
plt.show()


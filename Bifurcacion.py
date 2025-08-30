import numpy as np
import matplotlib.pyplot as plt
#r_min es el limite inferior en e
#r_max es el superior en r
#points: la cantidad de valores que se van a calcular
#N: numero de iteraciones}
#last: iteraciones finales
#X: valor incial

def bifurcation_diagram(r_min=2.5, r_max=4.0, points=5000, N=1000, last=100, X0=0.5):

    r_values = np.linspace(r_min, r_max, points)
    R = []
    X = []

    for r in r_values:
        x = X0
        # Iteraciones del inicio
        for h in range(N - last):
            x = r * x * (1 - x)
        # guardamos las ultimas
        for h in range(last):
            x = r * x * (1 - x)
            R.append(r)
            X.append(x)

    # grafica
    plt.figure(figsize=(10, 6))
    plt.plot(R, X, ',k', alpha=0.25)  # puntos negros pequeños
    plt.title("Diagrama de bifurcacion del mapa logistico")
    plt.xlabel("r")
    plt.ylabel("X")
    plt.grid(True, alpha=0.3)
    plt.show()

#llamar la funcion
bifurcation_diagram()

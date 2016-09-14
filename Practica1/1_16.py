# Genera los primeros n terminos de la secuencia xk+1 = 2.25 xk - 0.5 xk-1
from pylab import *
import matplotlib.pyplot  as pyplot

# Genera terminos en la secuencia
# n - numero de terminos a generar
def genera(n):
    terminos = [] # Lista de terminos
    terminos.append(1.0/3)
    terminos.append(1.0/12)
    for i in range(n-2):
        terminos.append((2.25*terminos[-1]) - (0.5*terminos[-2]))
    return terminos

# Grafica una lista de terminos de la serie
# l - lista a graficar
def grafica(l):
    fig = pyplot.figure() # Grafica
    ax = fig.add_subplot(1, 1, 1) # Subgrafica
    line = ax.plot(l, color='blue', lw=2) # Linea a graficar
    ax.set_yscale('log')
    pyplot.xlabel('k')
    pyplot.ylabel('xk')
    show()

grafica(genera(60))

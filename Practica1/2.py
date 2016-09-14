# Resuelve el problema 2 de la seccion 2.1 del libro Numerical Mathematics and
# Computing
from tabulate import tabulate

# Construye la tabla que se pide en el ejercicio
def tabla():
    # Puse cada tabla como un arreglo para facilitarme el trabajo
    regreso = []
    f = []
    g = []
    h = []
    for i in range(50):
        i += 1 # Porque la funcion range empieza en 0
        i = float(i)
        f.append(1/i)
        num_g = f[-1] # Siguiente elemento de g
        for j in range(int(i) - 1): 
            num_g += f[-1]
        g.append(num_g)
        h.append(i * f[-1])
        regreso.append([f[-1], g[-1], h[-1]])
    return regreso # Regresa lista de listas

tab = tabla()
print(tabulate(tab, headers=['f', 'g', 'h'], tablefmt='orgtbl'))

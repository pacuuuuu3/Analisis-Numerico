# Ejercicio 1.12 del libro Scientific computing: an introductory survey
from math import sqrt, pow, fabs

# Calcula la media del vector v
# v - vector
def media(v):
    n = len(v) # Longitud del vector
    if n == 0:
        return 0
    suma = 0.0 # Suma de todos los elementos del vector
    for elem in v:
        suma += elem
    return float(suma)/n

# Calcula la desviacion estandar con el primer metodo (two-pass formula)
# v - vector
def two_pass(v):
    n = len(v) # Longitud del vector
    m = media(v) # La media del vector
    suma = 0.0 # Suma utilizada para calcular la desviacion estandar
    for elem in v:
        suma += pow(elem - m, 2)
    cuadrado = 1.0 / (n-1) # Varianza
    cuadrado *= suma
    return sqrt(cuadrado)

# Calcula la desviacion estandar con el segundo metodo (one-pass formula)
# v - vector
def one_pass(v):
    n = len(v) # Longitud del vector
    m = media(v) # La media del vector
    m = pow(m, 2) # Elevamos la media al cuadrado
    suma = 0.0 # Suma utilizada para calcular la desviacion estandar
    contador = 0 # Número de sumando
    for elem in v:
        contador += 1
        suma += pow(elem, 2)
        suma -= contador*m
    cuadrado = 1.0 / (n-1) # Varianza
    cuadrado *= suma
    return sqrt(cuadrado)

l = [0.1, 0, 0.1, 10000000, 0.1, 0.1, 0.1]
print('Vector: ' + str(l))
print('Media: ' + str(media(l)))
print('Two pass: ' + str(two_pass(l)))
print('One pass: ' + str(one_pass(l)))
print('Diferencia : ' + str(fabs(two_pass(l) - one_pass(l))))

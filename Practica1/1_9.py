# Programa para computar la funcion exponencial utilizando la serie 1 + x +
# x^2/2! + ...
from numpy import exp

# Calcula la funcion exponencial e^x
def exponencial(x):
    suma = 1 + x # La suma hasta ahora
    suma_anterior = suma # La suma sin el ultimo sumando
    sumando_siguiente = x # Siguiente elemento a sumar
    contador = 2 # Para saber el numero de elemento a sumar
    while 1:
        sumando_siguiente *= float(x)/contador
        suma_anterior = suma
        suma += sumando_siguiente
        if suma == suma_anterior:
            break
        contador += 1
    return suma
        
x = input("Ingrese el numero del cual quiere calcular la exponencial:\n")
print(str(exponencial(float(x))))
y = exponencial(float(x)) - exp(float(x))
print('Dif: ' + str(y))

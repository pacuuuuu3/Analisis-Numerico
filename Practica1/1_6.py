# Problema 1.6 de "Numerical Mathematics and Computing"

from numpy import linspace

NUM_ITERACIONES = 10

# Primer metodo de suma (xk = xk-1 + h)
# a, b - Extremos del intervalo a sumar
# n - numero de elementos menos 1
def suma1(a, b, n):
    lista_x = [] # Lista de xi's
    lista_x.append(a)
    h = float(a + b)/n # Tamano del paso
    for num in linspace(a, b, n):
        lista_x.append(lista_x[-1] + h)
    return lista_x

# Segundo metodo de suma (xk = a + kh)
# a, b - Extremos del intervalo a sumar
# n - numero de elementos menos 1
def suma2(a, b, n):
    lista_x = [] # Lista de xi's
    h = float(a + b)/n # Tamano del paso
    k = 0 # Contador
    for num in linspace(a, b, n+1):
        lista_x.append(a + k*h)
        k += 1
    return lista_x

print('Ilustremos la diferencia entre ambos metodos con 10 numeros en el intervalo [0, 1]')
lista1 = suma1(0, 1, NUM_ITERACIONES)
lista2 = suma2(0, 1, NUM_ITERACIONES)
contador = 0
for num in lista1:
    print('Primer metodo: ' + 'x' + str(contador) + '= ' + str(num))
    print('Segundo metodo: ' + 'x' + str(contador) + '= ' + str(lista2[contador]))
    print('Diferencia:' + str(num - lista2[contador]))
    contador += 1

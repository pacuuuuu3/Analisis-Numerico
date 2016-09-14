# Programa para calcular los primeros n terminos de la secuencia dada en el
# ejercicio 1.7 del libro

# Calcula los primeros n terminos de la secuencia
# n - numero de terminos
def sec(n):
    secuencia = [] # Lista de terminos
    secuencia.append(11.0/2)
    secuencia.append(61.0/11)
    for i in range(n - 2):
        nuevo = 111 - (1130 - (3000.0/secuencia[-2]))/secuencia[-1]
        secuencia.append(nuevo)
    return secuencia

secuencia = sec(20)
contador = 1
for num in secuencia:
    print('x' + str(contador) + ': ' + str(num))
    contador += 1

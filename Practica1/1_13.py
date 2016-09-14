# Programa que calcula el interes compuesto
from math import exp, log, fabs

# Calcula el interes compuesto usando un loop
# a - cantidad invertida
# r - tasa de interes
# n - veces a componer el interes
def interes_loop(a, r, n):
    resultado = a # El numero que regresaremos
    for i in range(n):
        resultado *= (1.0 + (float(r)/n))
    return resultado

# Calcula el interes compuesto utilizando las funciones exp y log
# a - cantidad invertida
# r - tasa de interes
# n - veces a componer el interes
def interes_exp_log(a, r, n):
    return a * exp(n * log(1 + (r/n)))

a = 100
r = 0.05
n = [1, 4, 12, 365, 10000, 20000]
for numero in n:
    print('n = ' + str(numero))
    loop = interes_loop(a, r, numero)
    exp_log = interes_exp_log(a, r, numero)
    dif = loop - exp_log
    print('loop: ' + str(loop))
    print('exp_log: ' + str(exp_log))
    print('diferencia: ' + str(fabs(dif)))
    

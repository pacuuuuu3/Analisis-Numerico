# Programa que calcula el interes compuesto

# Calcula el interes compuesto usando un loop
# a - cantidad invertida
# r - tasa de interes
# n - veces a componer el interes
def interes_loop(a, r, n):
    resultado = a # El numero que regresaremos
    for i in range(n):
        resultado *= (1.0 + (float(r)/n))
    return resultado

a = 10
r = 0.0000000001
n = 10000001 
print(str(interes_loop(a, r, n)))
n = 11000001
print(str(interes_loop(a, r, n)))

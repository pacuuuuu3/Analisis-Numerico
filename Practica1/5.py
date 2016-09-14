# Problema 5 del libro Numerical Mathematics and Computing
import sys
from decimal import *

# Regresa el siguiente entero sin 0 en su representacion
def siguiente(i):
    cadena = str(i)
    longitud = len(cadena)
    if(cadena == '9'*longitud):
        return int('1'*(longitud+1))
    else:
        contador = -1
        while(cadena[contador] == '9'):
            new = list(cadena)
            new[contador] = '1'
            cadena = ''.join(new)
            contador -= 1
        new = list(cadena)
        new[contador] = chr(ord(new[contador]) + 1)
        nueva_cadena = ''.join(new)
        return int(nueva_cadena)
    
# Suma los reciprocos de todos los enteros que no contienen a '0'
def suma_reciprocos():
    suma = Decimal(0)
    try:
        inicial = 1
        while(inicial < sys.maxsize):
            anterior = suma
            suma += Decimal(1)/Decimal(inicial)
            if anterior == suma:
                break
            inicial = siguiente(inicial)
        return suma
    except:
        return suma

print(str(suma_reciprocos()))


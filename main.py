#Ejercicio 2

import math

area = float(input("Ingrese el lado del triangulo: "))

result = math.sqrt((3/4)*(area ** 2))

if result < 1000:
    print(f"""El area del triangulo es {result}""")

elif result > 1000:
    print(f"""DATOS NO VALIDOS""")
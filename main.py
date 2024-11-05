#Ejercicio 3

volt_1 = float(input("ingrese el primer voltaje: "))
volt_2 = float(input("ingrese el segundo voltaje: "))
volt_3 = float(input("ingrese el tercero voltaje: "))

result = (volt_1 + volt_2 + volt_3) / 3

if result < 115:
    print(f"""VOLTAJE CORRECTO""")

if result > 115 and result < 220:
    print(f"""ALTO VOLTAJE""")

if result > 220:
    print(f"""PELIGRO""")
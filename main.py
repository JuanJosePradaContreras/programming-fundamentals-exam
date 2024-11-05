#Ejercicio 1

volt_1 = int(input("ingrese el primer voltaje: "))
volt_2 = int(input("ingrese el segundo voltaje: "))
volt_3 = int(input("ingrese el tercero voltaje: "))
volt_4 = int(input("ingrese el cuarto voltaje: "))
volt_5 = int(input("ingrese el quinto voltaje: "))

result = (volt_1 + volt_2 + volt_3 + volt_4 + volt_5) / 5

if result > 220:
    print(f"""{result} es un voltaje alto""")
    
elif result < 220:
    print(f"""{result} es un voltaje correcto""")
import math
print("Hipotenusa")

def calcular_hipotenusa(a, b):
    return math.sqrt(a**2 + b**2)

cateto1 = float(input("Ingresa la longitud del primer cateto: "))
cateto2 = float(input("Ingresa la longitud del segundo cateto: "))

hipotenusa = calcular_hipotenusa(cateto1, cateto2)

print(f"La hipotenusa es: {hipotenusa}")
 




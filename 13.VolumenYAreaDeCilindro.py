import math
print("Volumen y Area de Cilindro")

radio = float(input("Ingresa el radio del cilindro: "))
altura = float(input("Ingresa la altura del cilindro: "))

volumen = math.pi * radio**2 * altura
area = 2 * math.pi * radio * altura

print(f"El volumen es: {volumen}")
print(f"La area es: {area}")
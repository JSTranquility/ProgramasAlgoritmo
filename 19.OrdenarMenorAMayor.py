print("Ordenar Menor a Mayor")

numeros = []

continuar = "S"

while continuar == "S":
    numero = int(input("Introduzca un numero (0 para finalizar): "))
    if numero == 0:
        continuar = "N"
    else:
        numeros.append(numero)
        
print(numeros)

numeros.sort()

print(numeros)
    
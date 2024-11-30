print("Contar y Sumar Pares")    

suma = 0
contador = 0

for i in range(1, 300):
    print(i)
    if i % 2 == 0:
        suma = suma + i
        contador = contador + 1

print("El numero de pares es", contador)
print("La sumatoria es", suma)
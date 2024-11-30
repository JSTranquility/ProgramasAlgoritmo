print("Sumatoria de numeros pares")

suma = 0
pares = 0

for i in range(1, 100):
    print(i)
    if i % 2 == 0:
        suma = suma + i
        pares = pares + 1   

print("El numero de pares es", pares)
print("La sumatoria es", suma)
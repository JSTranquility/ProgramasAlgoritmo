print("Multiplos de 5")
suma = 0
multiplos = 0

for i in range(1, 100):
    print(i)
    if i % 5 == 0:
        suma = suma + i
        multiplos = multiplos + 1
    
    
        
print("La sumatoria es", suma)
print("El numero de multiplos es", multiplos)
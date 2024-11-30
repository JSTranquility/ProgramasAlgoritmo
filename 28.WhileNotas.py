def calcular_promedio():
    suma_notas = 0
    cantidad_notas = 0
    
    while True:
        
        nota = float(input("Ingrese la nota (o 0 para finalizar): "))
        
        if nota == 0:
            break
        
        suma_notas += nota
        cantidad_notas += 1
    
    if cantidad_notas > 0:
        promedio = suma_notas / cantidad_notas
        print(f"El promedio de las notas es: {promedio:.2f}")
    else:
        print("No se ingresaron notas.")

calcular_promedio()

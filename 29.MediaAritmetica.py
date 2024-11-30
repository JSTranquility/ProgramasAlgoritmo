def calcular_media():
    suma = 0
    cantidad = 0
    
    while True:
        numero = float(input("Ingrese un número (o 0 para finalizar): "))
        
        if numero == 0:
            break
        
        suma += numero
        cantidad += 1
    
    if cantidad > 0:
        media = suma / cantidad
        print(f"La media aritmética es: {media:.2f}")
    else:
        print("No se ingresaron números.")
calcular_media()

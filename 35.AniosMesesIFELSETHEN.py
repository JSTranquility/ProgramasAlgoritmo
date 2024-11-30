
def convertir_dias():
    
    print("\n----- Conversión de Días -----\n")
    
    try:
        total_dias = int(input("Ingrese el número total de días: "))

        if total_dias < 0:
            print("Por favor, ingrese un número positivo.")
        else:

            anios = total_dias // 365
            dias_restantes = total_dias % 365

            if dias_restantes >= 30:
                meses = dias_restantes // 30
                dias_restantes %= 30
            else:
                meses = 0

            if dias_restantes >= 7:
                semanas = dias_restantes // 7
                dias_restantes %= 7
            else:
                semanas = 0

            print(f"\n{total_dias} días equivalen a:")
            print(f"Años: {anios}")
            print(f"Meses: {meses}")
            print(f"Semanas: {semanas}")
            print(f"Días: {dias_restantes}")
    
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    convertir_dias()


def convertir_dias():
    print("\n----- Conversión de Días -----\n")

    try:
        dias_totales = int(input("Ingrese el número total de días: "))

        if dias_totales < 0:
            print("Por favor, ingrese un número positivo.")
            return

        DIAS_EN_ANO = 365
        DIAS_EN_MES = 30
        DIAS_EN_SEMANA = 7

        anos = 0
        meses = 0
        semanas = 0
        dias_restantes = dias_totales

        while dias_restantes >= DIAS_EN_ANO:
            anos += 1
            dias_restantes -= DIAS_EN_ANO

        while dias_restantes >= DIAS_EN_MES:
            meses += 1
            dias_restantes -= DIAS_EN_MES

        while dias_restantes >= DIAS_EN_SEMANA:
            semanas += 1
            dias_restantes -= DIAS_EN_SEMANA

        # Imprimir resultados
        print(f"\n{dias_totales} días equivalen a:")
        print(f"{anos} año(s)")
        print(f"{meses} mes(es)")
        print(f"{semanas} semana(s)")
        print(f"{dias_restantes} día(s)")

    except ValueError:
        print("Por favor, ingrese un número entero válido.")

# Llamar a la función principal
if __name__ == "__main__":
    convertir_dias()

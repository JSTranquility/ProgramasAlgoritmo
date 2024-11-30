def calcular_nomina():
    tarifa_por_hora = 30000  # Tarifa en bolívares por hora trabajada
    total_obreros = 50       # Número total de obreros
    i = 1                    # Inicializar el contador de obreros
    
    # Usando un bucle WHILE para recorrer los 50 obreros
    while i <= total_obreros:
        
        horas_trabajadas = float(input(f"Ingrese las horas trabajadas por el obrero {i}: "))
        
        salario = horas_trabajadas * tarifa_por_hora
        
        print(f"El obrero {i} ha trabajado {horas_trabajadas} horas y debe recibir {salario:,.2f} Bolívares.")
        
        i += 1
        
calcular_nomina()

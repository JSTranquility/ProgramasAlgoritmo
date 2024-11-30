def calcular_nomina():
    tarifa_por_hora = 30000  
    total_obreros = 50      

    for i in range(1, total_obreros + 1):
        horas_trabajadas = float(input(f"Ingrese las horas trabajadas por el obrero {i}: "))
        
        salario = horas_trabajadas * tarifa_por_hora
        
        print(f"El obrero {i} ha trabajado {horas_trabajadas} horas y debe recibir {salario:,.2f} Bolívares.")
        
calcular_nomina()

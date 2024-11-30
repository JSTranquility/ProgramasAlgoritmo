def calcular_monto_estacionamiento(hora_entrada, hora_salida):

    entrada_hora, entrada_minuto = map(int, hora_entrada.split(":"))
    salida_hora, salida_minuto = map(int, hora_salida.split(":"))
    

    minutos_entrada = entrada_hora * 60 + entrada_minuto
    minutos_salida = salida_hora * 60 + salida_minuto
    

    diferencia_minutos = minutos_salida - minutos_entrada
    

    if diferencia_minutos <= 0:
        diferencia_minutos += 24 * 60  
    
  
    horas_totales = (diferencia_minutos + 59) // 60  

    if horas_totales <= 1:
        monto = 1000  
    else:
        monto = 1000 + (horas_totales - 1) * 600  
    
    return monto

hora_entrada = input("Ingrese la hora de entrada (formato militar HH:MM): ")
hora_salida = input("Ingrese la hora de salida (formato militar HH:MM): ")

monto_a_pagar = calcular_monto_estacionamiento(hora_entrada, hora_salida)
print(f"El monto a pagar por el estacionamiento es: {monto_a_pagar} bolívares.")

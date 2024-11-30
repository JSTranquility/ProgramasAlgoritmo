def calcular_minutos_en_horas(horas):
   
    minutos_por_hora = 60
  
    minutos = horas * minutos_por_hora
    return minutos

horas = 5

minutos = calcular_minutos_en_horas(horas)

print(f"En {horas} horas hay {minutos} minutos.")

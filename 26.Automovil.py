def convertir_velocidad(km_por_hora):
    # Sabemos que 1 km/h = 1000 metros / 3600 segundos
    metros_por_segundo = km_por_hora * 1000 / 3600
    return metros_por_segundo


km_por_hora = float(input("Ingrese la velocidad en kilómetros por hora (km/h): "))


m_por_s = convertir_velocidad(km_por_hora)


print(f"La velocidad de {km_por_hora} km/h es equivalente a {m_por_s:.2f} m/s.")

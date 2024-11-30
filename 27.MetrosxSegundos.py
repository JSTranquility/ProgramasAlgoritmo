def convertir_velocidad(m_por_s):

    km_por_hora = m_por_s * 3600 / 1000
    return km_por_hora


m_por_s = float(input("Ingrese la velocidad en metros por segundo (m/s): "))

km_por_hora = convertir_velocidad(m_por_s)

print(f"La velocidad de {m_por_s} m/s es equivalente a {km_por_hora:.2f} km/h.")

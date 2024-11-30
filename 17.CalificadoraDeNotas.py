print    ("Calificadora de Notas")

nota = int(input("Ingresa la nota: "))

nuevanota = ""

if nota >= 19 and nota <= 20:  
    nuevanota = "A"
elif nota >= 16 and nota <= 18:
    nuevanota = "B"
elif nota >= 13 and nota <= 15:
    nuevanota = "C"
elif nota >= 10 and nota <= 12:
    nuevanota = "D"
else:
    nuevanota = "F"

print(f"La nota es: {nota}")

print(f"La calificacion es: {nuevanota}")
    
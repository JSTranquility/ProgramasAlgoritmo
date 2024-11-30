print("Contar Números en Rango")
Contador50_75 = 0
ContadorMayor80 = 0
ContadorMenor30 = 0

while True:  
    numero = int(input("Introduzca un número (0 para finalizar): "))
    if numero == 0:
        break  

    if numero < 30:
        ContadorMenor30 += 1
    elif 50 <= numero <= 75:  
        Contador50_75 += 1
    elif numero > 80:
        ContadorMayor80 += 1

print("El número de números menores a 30 es:", ContadorMenor30)
print("El número de números mayores a 80 es:", ContadorMayor80)
print("El número de números entre 50 y 75 es:", Contador50_75)

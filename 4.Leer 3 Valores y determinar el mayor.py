print("Leer 3 valores")

print("Ingrese un numero")
a = int(input())

print("Ingrese otro numero")
b = int(input())

print("Ingrese otro numero")
c = int(input())

if a > b and a > c:
    print(a, "es mayor")
elif b > a and b > c:
    print(b, "es mayor")
elif c > a and c > b:
    print(c, "es mayor")
else:
    print("Los valores son iguales")
print("Indicar el mayor de 4")

def mayor(a, b, c, d):
    if a > b and a > c and a > d:
        print(a, "es mayor")
    elif b > a and b > c and b > d:
        print(b, "es mayor")
    elif c > a and c > b and c > d:
        print(c, "es mayor")
    elif d > a and d > b and d > c:
        print(d, "es mayor")
    else:
        print("Los valores son iguales")

print("Ingrese un numero")
a = int(input())

print("Ingrese otro numero")
b = int(input())

print("Ingrese otro numero")
c = int(input())

print("Ingrese otro numero")
d = int(input())        

mayor(a, b, c, d)   
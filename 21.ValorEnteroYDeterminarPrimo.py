
def es_primo(n):
    
    if n <= 1:
        return False
  
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


N = int(input("Ingrese un número entero positivo: "))

if es_primo(N):
    print(f"{N} es un número primo.")
else:
    print(f"{N} no es un número primo.")


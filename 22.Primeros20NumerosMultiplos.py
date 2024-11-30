def primeros_multiplos_de_2():
  
    multiplos = []
    

    for i in range(1, 21):
        multiplos.append(i * 2)
    
    return multiplos

multiples = primeros_multiplos_de_2()
print("Los primeros 20 múltiplos de 2 son:", multiples)

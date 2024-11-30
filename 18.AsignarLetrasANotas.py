def asignar_letras_notas():
    continuar = "S"  
    
    while continuar == "S":
 
        nota = int(input("Introduce la nota (0 para salir): "))
        
        if nota == 0:
            continuar = "N"  
        else:
           
            if 19 <= nota <= 28:
                nueva_nota = "A"
            elif 15 <= nota <= 18:
                nueva_nota = "B"
            elif 13 <= nota <= 14:
                nueva_nota = "C"
            elif 10 <= nota <= 12:
                nueva_nota = "D"
            elif 0 <= nota <= 9:
                nueva_nota = "F"
            else:
                nueva_nota = "E"  
            
            print(f"La nota ingresada es: {nota}")
            
            print(f"La nueva nota es: {nueva_nota}")


asignar_letras_notas()
